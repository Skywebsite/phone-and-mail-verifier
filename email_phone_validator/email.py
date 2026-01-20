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
    
    # Split email into local and domain parts
    if '@' not in email:
        return False
    
    parts = email.split('@')
    if len(parts) != 2:
        return False
    
    local_part, domain_part = parts
    
    # Validate local part
    # Must not be empty, must start and end with alphanumeric
    # Can contain dots, hyphens, underscores, and plus signs in between
    if not local_part or len(local_part) == 0:
        return False
    
    # Local part should start and end with alphanumeric
    if not local_part[0].isalnum() or not local_part[-1].isalnum():
        return False
    
    # Local part can contain alphanumeric, dots, hyphens, underscores, plus signs
    # Since start/end are already validated as alphanumeric, just check all chars are valid
    if not re.match(r'^[a-zA-Z0-9._+-]+$', local_part):
        return False
    
    # Check for consecutive dots in local part
    if '..' in local_part:
        return False
    
    # Validate domain part
    if not domain_part or '.' not in domain_part:
        return False
    
    # Domain should have valid structure
    domain_pattern = r'^[a-zA-Z0-9]([a-zA-Z0-9.-]*[a-zA-Z0-9])?\.[a-zA-Z]{2,}$'
    if not re.match(domain_pattern, domain_part):
        return False
    
    # Check for consecutive dots in domain
    if '..' in domain_part:
        return False
    
    return True

