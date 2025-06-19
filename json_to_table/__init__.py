"""
JSON to Table Converter

A Python library for converting JSON data into formatted tables with support for both simple and ASCII border styles.
"""

from .json_to_table import json_to_table
from .lib import TableStyle

__version__ = "1.0.0"
__author__ = "Your Name"
__all__ = ["json_to_table", "TableStyle"] 