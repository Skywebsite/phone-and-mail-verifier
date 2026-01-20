# email-phone-validator

A simple, production-ready Python package for validating email addresses and phone numbers.

## Features

- ✅ **Email Validation**: Validate email addresses using regex patterns
- ✅ **Phone Validation**: Validate phone numbers using the `phonenumbers` library
- ✅ **Country Support**: Default country is India (IN), but supports any country code
- ✅ **Clean API**: Simple and intuitive functions
- ✅ **Well Tested**: Comprehensive unit tests included
- ✅ **Production Ready**: Follows Python packaging best practices

## Installation

```bash
pip install phone-and-mail-verifier==0.1.1
```

## Quick Start >>>

```python
from email_phone_validator import validate_email, validate_phone

# Validate email
print(validate_email("test@gmail.com"))      # True
print(validate_email("invalid.email"))       # False

# Validate phone (default country: India)
print(validate_phone("9876543210"))          # True
print(validate_phone("+919876543210"))       # True
print(validate_phone("12345"))               # False

# Validate phone for other countries
print(validate_phone("+12025551234", "US"))  # True
print(validate_phone("2025551234", "US"))    # True
```

## Usage Examples

### Email Validation

```python
from email_phone_validator import validate_email

# Valid emails
validate_email("user@example.com")           # True
validate_email("john.doe@company.co.uk")     # True
validate_email("user+tag@example.com")       # True

# Invalid emails
validate_email("invalid.email")              # False
validate_email("@example.com")               # False
validate_email("user@")                      # False
```

### Phone Validation

```python
from email_phone_validator import validate_phone

# Indian phone numbers (default country)
validate_phone("9876543210")                 # True
validate_phone("+919876543210")              # True
validate_phone("919876543210")               # True

# US phone numbers
validate_phone("+12025551234", "US")         # True
validate_phone("2025551234", "US")           # True

# UK phone numbers
validate_phone("+447911123456", "GB")        # True
validate_phone("07911123456", "GB")          # True

# Invalid phone numbers
validate_phone("12345", "IN")                # False
validate_phone("abc1234567", "IN")           # False
```

### Combined Usage

```python
from email_phone_validator import validate_email, validate_phone

def validate_user_data(email, phone, country="IN"):
    """Validate user email and phone number."""
    email_valid = validate_email(email)
    phone_valid = validate_phone(phone, country)
    
    if email_valid and phone_valid:
        return True, "All validations passed"
    else:
        errors = []
        if not email_valid:
            errors.append("Invalid email address")
        if not phone_valid:
            errors.append("Invalid phone number")
        return False, ", ".join(errors)

# Example usage
is_valid, message = validate_user_data(
    email="user@example.com",
    phone="9876543210",
    country="IN"
)
print(f"Validation: {is_valid}, Message: {message}")
```

## API Reference

### `validate_email(email: str) -> bool`

Validates an email address using regex patterns.

**Parameters:**
- `email` (str): The email address to validate

**Returns:**
- `bool`: `True` if the email is valid, `False` otherwise

### `validate_phone(phone: str, country: str = "IN") -> bool`

Validates a phone number for a given country using the `phonenumbers` library.

**Parameters:**
- `phone` (str): The phone number to validate (can be with or without country code)
- `country` (str): ISO country code (default: "IN" for India)
  - Examples: "US", "GB", "IN", "AU", "CA", etc.

**Returns:**
- `bool`: `True` if the phone number is valid, `False` otherwise

## Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/email-phone-validator.git
cd email-phone-validator

# Install in development mode
pip install -e .

# Install development dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=email_phone_validator

# Run specific test file
pytest tests/test_email.py
pytest tests/test_phone.py
```

### Building the Package

```bash
# Install build tools
pip install build twine

# Build the package
python -m build

# This creates:
# - dist/email_phone_validator-0.1.0.tar.gz
# - dist/email_phone_validator-0.1.0-py3-none-any.whl
```

### Publishing to PyPI

1. **Create a PyPI account**: https://pypi.org/account/register/

2. **Upload the package**:
   ```bash
   twine upload dist/*
   ```

3. **Test the installation**:
   ```bash
   pip install phone-and-mail-verifier==0.1.1
   ```

## Requirements

- Python >= 3.7
- phonenumbers >= 8.13.0

## Supported Countries

The phone validation supports all countries supported by the `phonenumbers` library, including but not limited to:

- India (IN) - Default
- United States (US)
- United Kingdom (GB)
- Australia (AU)
- Canada (CA)
- And many more...

For a complete list, refer to the [phonenumbers library documentation](https://github.com/daviddrysdale/python-phonenumbers).

## License

MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Your Name - skywebdev123@gmail.com

## Acknowledgments

- Uses [phonenumbers](https://github.com/daviddrysdale/python-phonenumbers) library for phone validation
- Built with ❤️ for the Python community

