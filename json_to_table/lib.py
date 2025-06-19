"""
Core library functions for JSON to table conversion.
"""

import json
from typing import Any, List, Union, Dict
from enum import Enum
from .constants import WS, ES, FORMAT


class TableStyle(Enum):
    """Table style options."""
    SIMPLE = "simple"
    ASCII = "ascii"


def add_spaces(text: str, space_count: int) -> str:
    """Add specified number of spaces to a string."""
    for _ in range(space_count):
        text += WS
    return text


def remove_double_quotes(value: str) -> str:
    """Remove double quotes from a string."""
    return value.replace('"', ' ')


def create_ascii_border(start_points: List[int]) -> str:
    """Create ASCII border for table."""
    border_parts = []
    for i, point in enumerate(start_points):
        if i == 0:
            border_parts.append('-' * (start_points[1] - start_points[0]))
        elif i == len(start_points) - 1:
            continue
        else:
            border_parts.append('-' * (start_points[i + 1] - start_points[i]))
    
    return '+' + '+'.join(border_parts) + '+'


def format_complex_value(value: Any) -> str:
    """Format complex values for better display."""
    if value is None:
        return 'null'
    
    if not isinstance(value, (dict, list)):
        return str(value)
    
    if isinstance(value, list):
        if len(value) == 0:
            return '[]'
        return '\n'.join([
            format_complex_value(item) if isinstance(item, (dict, list)) else str(item)
            for item in value
        ])
    
    # Handle dictionary
    entries = []
    for k, v in value.items():
        if isinstance(v, (dict, list)):
            entries.append(f"{k}: {format_complex_value(v)}")
        else:
            entries.append(f"{k}: {v}")
    
    return '{' + '\n'.join(entries) + '}'


def wrap_text(text: str, max_width: int) -> List[str]:
    """Wrap text to fit within specified width."""
    if not text or len(text) <= max_width:
        return [text or '']
    
    # Split by newlines first to preserve array/object structure
    lines = text.split('\n')
    wrapped_lines = []
    
    for line in lines:
        if len(line) <= max_width:
            wrapped_lines.append(line)
        else:
            words = line.split(' ')
            current_line = ''
            
            for word in words:
                if len(current_line + word) <= max_width:
                    current_line += (' ' if current_line else '') + word
                else:
                    if current_line:
                        wrapped_lines.append(current_line)
                    current_line = word
            
            if current_line:
                wrapped_lines.append(current_line)
    
    return wrapped_lines


def get_row(headers: List[str], start_points: List[int], is_header_row: bool, obj: Dict[str, Any] = None) -> List[str]:
    """Generate a formatted row for the table."""
    max_width = 25
    rows = []
    max_lines = 1
    
    # First pass: calculate max lines needed
    for header in headers:
        value = header if is_header_row else obj[header]
        formatted_value = format_complex_value(value) if isinstance(value, (dict, list)) else str(value)
        wrapped_lines = wrap_text(formatted_value, max_width)
        max_lines = max(max_lines, len(wrapped_lines))
    
    # Generate all lines for the row
    for line_index in range(max_lines):
        row = ES
        for i, header in enumerate(headers):
            value = header if is_header_row else obj[header]
            formatted_value = format_complex_value(value) if isinstance(value, (dict, list)) else str(value)
            wrapped_lines = wrap_text(formatted_value, max_width)
            line_content = wrapped_lines[line_index] if line_index < len(wrapped_lines) else ''
            row += line_content
            space_count = start_points[i + 1] - len(row)
            row = add_spaces(row, space_count)
        rows.append(row)
    
    return rows


def get_rows(data: List[Dict[str, Any]], headers: List[str], start_points: List[int], style: TableStyle = TableStyle.SIMPLE) -> List[str]:
    """Generate all rows for the table."""
    rows = []
    
    if style == TableStyle.ASCII:
        # Add top border
        rows.append(create_ascii_border(start_points))
        
        # Add header row with borders
        header_rows = get_row(headers, start_points, True)
        for row in header_rows:
            rows.append('|' + row + '|')
        
        # Add separator
        rows.append(create_ascii_border(start_points))
        
        # Add data rows with borders
        for obj in data:
            data_rows = get_row(headers, start_points, False, obj)
            for row in data_rows:
                rows.append('|' + row + '|')
        
        # Add bottom border
        rows.append(create_ascii_border(start_points))
    else:
        # Original simple style
        header_rows = get_row(headers, start_points, True)
        rows.extend(header_rows)
        for obj in data:
            data_rows = get_row(headers, start_points, False, obj)
            rows.extend(data_rows)
    
    return rows


def get_start_point(header: str, data: List[Dict[str, Any]], start_point: int) -> int:
    """Calculate start point for a column."""
    lengths = [len(header)]
    for obj in data:
        if obj[header] is None:
            lengths.append(4)
        else:
            value = obj[header]
            formatted_value = format_complex_value(value) if isinstance(value, (dict, list)) else value
            lengths.append(len(str(formatted_value)))
    
    start_point += max(lengths) + 5
    return start_point


def get_start_points(data: List[Dict[str, Any]], headers: List[str]) -> List[int]:
    """Calculate start points for all columns."""
    start_points = [0]
    start_point = 0

    for header in headers:
        lengths = [len(header)]
        for obj in data:
            if obj[header] is None:
                lengths.append(4)
            else:
                value = obj[header]
                formatted_value = format_complex_value(value) if isinstance(value, (dict, list)) else str(value)
                # Calculate width based on wrapped lines
                wrapped_lines = wrap_text(formatted_value, 25)
                max_line_length = max(len(line) for line in wrapped_lines)
                lengths.append(max_line_length)
        
        # Add padding for better readability
        start_point += max(lengths) + 4
        start_points.append(start_point)

    return start_points


def get_data(params: Any) -> List[Dict[str, Any]]:
    """Process and validate input data."""
    try:
        if not isinstance(params, list):
            params = [params]
        
        # Deep copy the data to avoid modifying the original
        return json.loads(json.dumps(params))
    except (json.JSONDecodeError, TypeError) as error:
        print(f"Error parsing data: {error}")
        return [] 