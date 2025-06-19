# How to Publish Your Python Package to PyPI

This guide will walk you through the process of publishing your `json-to-table` package to PyPI (Python Package Index).

## Prerequisites

1. **Python 3.7+** installed on your system
2. **pip** and **setuptools** installed
3. **twine** for uploading to PyPI
4. **PyPI account** (TestPyPI for testing, PyPI for production)

## Step 1: Install Required Tools

```bash
pip install --upgrade pip setuptools wheel twine
```

## Step 2: Create PyPI Accounts

### TestPyPI (for testing)

1. Go to https://test.pypi.org/account/register/
2. Create an account
3. Verify your email

### PyPI (for production)

1. Go to https://pypi.org/account/register/
2. Create an account
3. Enable two-factor authentication (recommended)

## Step 3: Prepare Your Package

### Update Package Information

1. **Update `setup.py`** with your information:

   - Replace `"Your Name"` with your actual name
   - Replace `"your.email@example.com"` with your email
   - Replace `"yourusername"` with your GitHub username
   - Update the URL to point to your actual repository

2. **Update `json_to_table/__init__.py`**:

   - Replace `"Your Name"` with your actual name

3. **Update `LICENSE`**:
   - Replace `"Your Name"` with your actual name

### Test Your Package Locally

```bash
# Install in development mode
pip install -e .

# Test the package
python test_example.py
```

## Step 4: Build Your Package

```bash
# Clean previous builds
rm -rf build/ dist/ *.egg-info/

# Build the package
python setup.py sdist bdist_wheel
```

This creates:

- `dist/json-to-table-1.0.0.tar.gz` (source distribution)
- `dist/json_to_table-1.0.0-py3-none-any.whl` (wheel distribution)

## Step 5: Test on TestPyPI

### Upload to TestPyPI

```bash
# Upload to TestPyPI
twine upload --repository testpypi dist/*
```

You'll be prompted for your TestPyPI username and password.

### Test Installation from TestPyPI

```bash
# Create a new virtual environment for testing
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate

# Install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ json-to-table

# Test the package
python -c "from json_to_table import json_to_table; print('Package works!')"
```

## Step 6: Publish to PyPI

Once you've tested on TestPyPI and everything works:

```bash
# Upload to PyPI
twine upload dist/*
```

You'll be prompted for your PyPI username and password.

## Step 7: Verify Installation

```bash
# Create a new virtual environment
python -m venv prod_env
source prod_env/bin/activate  # On Windows: prod_env\Scripts\activate

# Install from PyPI
pip install json-to-table

# Test the package
python -c "from json_to_table import json_to_table; print('Package published successfully!')"
```

## Step 8: Update Your Package

When you want to update your package:

1. **Update version** in `json_to_table/__init__.py`
2. **Update version** in `setup.py` (if using static version)
3. **Build new distribution**:
   ```bash
   rm -rf build/ dist/ *.egg-info/
   python setup.py sdist bdist_wheel
   ```
4. **Upload to PyPI**:
   ```bash
   twine upload dist/*
   ```

## Troubleshooting

### Common Issues

1. **Package name already exists**: Choose a different name or add a suffix
2. **Authentication errors**: Make sure you're using the correct credentials
3. **Build errors**: Check that all required files are present
4. **Import errors**: Verify your package structure is correct

### Useful Commands

```bash
# Check package contents
tar -tzf dist/json-to-table-1.0.0.tar.gz

# Validate package
twine check dist/*

# Check package metadata
python setup.py check --metadata --strict
```

## Security Best Practices

1. **Use API tokens** instead of passwords for PyPI
2. **Enable two-factor authentication** on PyPI
3. **Use virtual environments** for testing
4. **Never commit credentials** to version control

## Additional Resources

- [PyPI Packaging Guide](https://packaging.python.org/tutorials/packaging-projects/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [Setuptools Documentation](https://setuptools.readthedocs.io/)

## Package Structure Summary

Your final package structure should look like this:

```
json-to-table/
├── json_to_table/
│   ├── __init__.py
│   ├── constants.py
│   ├── lib.py
│   └── json_to_table.py
├── setup.py
├── README.md
├── LICENSE
├── MANIFEST.in
├── test_example.py
└── PUBLISH_GUIDE.md
```

## Next Steps

After publishing:

1. **Create a GitHub repository** for your package
2. **Add documentation** and examples
3. **Set up CI/CD** for automated testing and deployment
4. **Monitor downloads** and user feedback
5. **Maintain and update** your package regularly
