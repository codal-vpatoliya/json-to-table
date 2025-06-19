"""
Setup script for json-to-table package.
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read version from __init__.py
def get_version():
    with open("json_to_table/__init__.py", "r", encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("__version__"):
                return line.split("=")[1].strip().strip('"\'')
    return "1.0.0"

setup(
    name="json-to-table",
    version=get_version(),
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python library for converting JSON data into formatted tables",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/json-to-table",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
    },
    keywords="json, table, formatting, ascii, console, terminal",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/json-to-table/issues",
        "Source": "https://github.com/yourusername/json-to-table",
        "Documentation": "https://github.com/yourusername/json-to-table#readme",
    },
) 