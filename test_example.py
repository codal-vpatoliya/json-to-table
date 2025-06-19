#!/usr/bin/env python3
"""
Test example for the json-to-table package.
"""

from json_to_table import json_to_table, TableStyle

def main():
    # Test data
    simple_data = [
        {"name": "John", "age": 30, "city": "New York"},
        {"name": "Jane", "age": 25, "city": "Los Angeles"},
        {"name": "Bob", "age": 35, "city": "Chicago"}
    ]

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
        },
        {
            "name": "Jane",
            "age": 25,
            "address": {
                "street": "456 Oak Ave",
                "city": "Los Angeles",
                "zip": "90210"
            },
            "hobbies": ["painting", "dancing"]
        }
    ]

    nested_data = [
        {
            "id": 1,
            "user": {
                "name": "Alice",
                "email": "alice@example.com"
            },
            "orders": [
                {"item": "Book", "price": 15.99},
                {"item": "Pen", "price": 2.50}
            ]
        },
        {
            "id": 2,
            "user": {
                "name": "Bob",
                "email": "bob@example.com"
            },
            "orders": [
                {"item": "Laptop", "price": 999.99}
            ]
        }
    ]

    print("=== Simple Style ===")
    print(json_to_table(simple_data, "simple"))
    print("\n")

    print("=== ASCII Style ===")
    print(json_to_table(simple_data, "ascii"))
    print("\n")

    print("=== Complex Data (Simple Style) ===")
    print(json_to_table(complex_data, "simple"))
    print("\n")

    print("=== Complex Data (ASCII Style) ===")
    print(json_to_table(complex_data, "ascii"))
    print("\n")

    print("=== Nested Data (Simple Style) ===")
    print(json_to_table(nested_data, "simple"))
    print("\n")

    print("=== Nested Data (ASCII Style) ===")
    print(json_to_table(nested_data, "ascii"))

if __name__ == "__main__":
    main() 