"""
Phone number validation module using the phonenumbers library.
"""

import phonenumbers
from phonenumbers import NumberParseException


def is_valid_phone(phone: str, country: str = "IN") -> bool:
    """
    Validate a phone number using the phonenumbers library.
    
    This function validates phone numbers based on the country code provided.
    Default country is India (IN).
    
    Args:
        phone (str): The phone number to validate (can be with or without country code)
        country (str): ISO country code (default: "IN" for India)
                      Examples: "US", "GB", "IN", "AU"
        
    Returns:
        bool: True if the phone number is valid, False otherwise
        
    Examples:
        >>> is_valid_phone("9876543210", "IN")
        True
        >>> is_valid_phone("+919876543210", "IN")
        True
        >>> is_valid_phone("1234567890", "US")
        False  # Invalid US number
    """
    if not phone or not isinstance(phone, str):
        return False
    
    # Remove whitespace
    phone = phone.strip()
    
    if not phone:
        return False
    
    try:
        # Parse the phone number with the given country code
        parsed_number = phonenumbers.parse(phone, country)
        
        # Check if the number is valid for the given country
        is_valid = phonenumbers.is_valid_number(parsed_number)
        
        # Optionally, check if the number is possible (less strict check)
        # is_possible = phonenumbers.is_possible_number(parsed_number)
        
        return is_valid
        
    except NumberParseException:
        # If parsing fails, the number is invalid
        return False
    except Exception:
        # Catch any other unexpected errors
        return False

