"""
Main validator module that provides a clean API for email and phone validation.
"""

from .email import is_valid_email
from .phone import is_valid_phone


def validate_email(email: str) -> bool:
    """
    Validate an email address.
    
    This is the main API function for email validation. It provides a clean
    interface to check if an email address is valid.
    
    Args:
        email (str): The email address to validate
        
    Returns:
        bool: True if the email is valid, False otherwise
        
    Examples:
        >>> validate_email("user@example.com")
        True
        >>> validate_email("invalid-email")
        False
    """
    return is_valid_email(email)


def validate_phone(phone: str, country: str = "IN") -> bool:
    """
    Validate a phone number.
    
    This is the main API function for phone number validation. It provides a clean
    interface to check if a phone number is valid for a given country.
    
    Args:
        phone (str): The phone number to validate
        country (str): ISO country code (default: "IN" for India)
        
    Returns:
        bool: True if the phone number is valid, False otherwise
        
    Examples:
        >>> validate_phone("9876543210", "IN")
        True
        >>> validate_phone("+919876543210")
        True
        >>> validate_phone("12345", "IN")
        False
    """
    return is_valid_phone(phone, country)

