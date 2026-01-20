"""
Email validation module using regex patterns.
"""

import re


def is_valid_email(email: str) -> bool:
    """
    Validate an email address using regex pattern.
    
    This function checks if the email address follows the standard email format:
    - Contains @ symbol
    - Has a valid domain name
    - Follows basic email structure rules
    
    Args:
        email (str): The email address to validate
        
    Returns:
        bool: True if the email is valid, False otherwise
        
    Examples:
        >>> is_valid_email("test@gmail.com")
        True
        >>> is_valid_email("invalid.email")
        False
    """
    if not email or not isinstance(email, str):
        return False
    
    # Remove leading/trailing whitespace
    email = email.strip()
    
    # Basic email regex pattern
    # This pattern checks for:
    # - Local part (before @): alphanumeric, dots, hyphens, underscores, plus signs
    # - @ symbol
    # - Domain part (after @): alphanumeric, dots, hyphens
    # - Top-level domain: 2-6 letters
    pattern = r'^[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$'
    
    # More comprehensive pattern for better validation
    # Allows for more complex email formats
    comprehensive_pattern = r'^[a-zA-Z0-9]([a-zA-Z0-9._-]*[a-zA-Z0-9])?@[a-zA-Z0-9]([a-zA-Z0-9.-]*[a-zA-Z0-9])?\.[a-zA-Z]{2,}$'
    
    # Check if email matches the pattern
    if re.match(comprehensive_pattern, email):
        # Additional checks
        # Email should not start or end with dot
        if email.startswith('.') or email.endswith('.'):
            return False
        # Email should not have consecutive dots
        if '..' in email:
            return False
        # @ symbol should appear only once
        if email.count('@') != 1:
            return False
        
        return True
    
    return False

