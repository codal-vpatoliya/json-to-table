"""
Main function for converting JSON to table format.
"""

from typing import Union, Any
from .lib import get_start_points, get_rows, get_data, TableStyle


def json_to_table(params: Any, style: Union[str, TableStyle] = "simple") -> str:
    """
    Convert JSON data to a formatted table string.
    
    Args:
        params: The data to convert (dict, list of dicts, or list)
        style: Table style - "simple" (default) or "ascii"
    
    Returns:
        A string containing the formatted table
    """
    try:
        # Convert string style to enum if needed
        if isinstance(style, str):
            style = TableStyle(style)
        
        data = get_data(params)
        
        if not data or len(data) == 0:
            return "No data to display"
        
        headers = list(data[0].keys())
        if len(headers) == 0:
            return "No headers found in data"
        
        start_points = get_start_points(data, headers)
        rows = get_rows(data, headers, start_points, style)
        return '\n'.join(rows)
    
    except Exception as error:
        print(f"Error converting JSON to table: {error}")
        return "Error: Unable to convert data to table format"


# Export for compatibility
__all__ = ["json_to_table", "TableStyle"] 