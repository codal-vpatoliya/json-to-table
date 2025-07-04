# JSON to Table Converter

A Python library for converting JSON data into formatted tables with support for both simple and ASCII border styles.

## Features

- Convert JSON objects and arrays to formatted tables
- Support for complex nested objects and arrays
- Two table styles: simple and ASCII with borders
- Automatic text wrapping for long content
- Type hints and comprehensive error handling
- No external dependencies

## Installation

```bash
pip install json-to-table
```

## Usage

### Basic Usage

```python
from json_to_table import json_to_table

data = [
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Jane", "age": 25, "city": "Los Angeles"}
]

# Simple style (default)
simple_table = json_to_table(data)
print(simple_table)

# ASCII style with borders
ascii_table = json_to_table(data, "ascii")
print(ascii_table)
```

### Complex Data

The library handles complex nested objects and arrays:

```python
complex_data = [
    {
        "name": "John",
        "age": 30,
        "address": {
            "street": "123 Main St",
            "city": "New York",
            "zip": "10001"
        },
        "hobbies": ["reading", "swimming", "coding"]
    }
]

table = json_to_table(complex_data, "ascii")
print(table)
```

## API Reference

### `json_to_table(params: Any, style: Union[str, TableStyle] = "simple") -> str`

Converts JSON data to a formatted table string.

**Parameters:**

- `params`: The data to convert (dict, list of dicts, or list)
- `style`: Optional table style - `"simple"` (default) or `"ascii"`

**Returns:**

- A string containing the formatted table

**Table Styles:**

1. **Simple Style**: Clean, minimal formatting without borders
2. **ASCII Style**: Traditional table with ASCII borders and separators

## Examples

### Simple Data Output

```
name    age     city
John    30      New York
Jane    25      Los Angeles
```

### ASCII Style Output

```
+------+-----+-------------+
| name | age | city        |
+------+-----+-------------+
| John | 30  | New York    |
| Jane | 25  | Los Angeles |
+------+-----+-------------+
```

### Complex Data Handling

The library automatically formats nested objects and arrays:

```
+------+-----+------------------------+------------------+
| name | age | address                | hobbies          |
+------+-----+------------------------+------------------+
| John | 30  | street: 123 Main St    | reading          |
|      |     | city: New York         | swimming         |
|      |     | zip: 10001             | coding           |
+------+-----+------------------------+------------------+
```

## Development

### Install in Development Mode

```bash
git clone https://github.com/yourusername/json-to-table.git
cd json-to-table
pip install -e .
```

### Run Tests

```bash
pip install -e ".[dev]"
pytest
```

## TypeScript to Python Conversion

This package is a direct conversion of the TypeScript `json-to-table` library, maintaining the same API and functionality:

- `TableStyle` enum → `TableStyle` enum
- `jsonToTable()` function → `json_to_table()` function
- Same table formatting logic and styles
- Identical output format

## Error Handling

The library includes comprehensive error handling:

- Invalid JSON data returns an error message
- Empty data arrays return "No data to display"
- Missing headers return "No headers found in data"

## License

MIT License
