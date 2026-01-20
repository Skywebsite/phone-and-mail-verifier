"""
Unit tests for email validation.
"""

import pytest
from email_phone_validator.email import is_valid_email


class TestEmailValidation:
    """Test cases for email validation."""
    
    def test_valid_emails(self):
        """Test various valid email formats."""
        valid_emails = [
            "test@gmail.com",
            "user@example.com",
            "john.doe@company.co.uk",
            "user+tag@example.com",
            "user_name@example-domain.com",
            "123@example.com",
            "a@b.co",
        ]
        
        for email in valid_emails:
            assert is_valid_email(email) == True, f"{email} should be valid"
    
    def test_invalid_emails(self):
        """Test various invalid email formats."""
        invalid_emails = [
            "invalid.email",
            "@example.com",
            "user@",
            "user@.com",
            "user..name@example.com",
            ".user@example.com",
            "user@example.",
            "",
            " ",
            None,
        ]
        
        for email in invalid_emails:
            if email is None:
                assert is_valid_email(email) == False, "None should be invalid"
            else:
                assert is_valid_email(email) == False, f"{email} should be invalid"
    
    def test_email_with_whitespace(self):
        """Test that emails with leading/trailing whitespace are handled."""
        assert is_valid_email("  test@gmail.com  ") == True
        assert is_valid_email(" test@gmail.com") == True
        assert is_valid_email("test@gmail.com ") == True
    
    def test_non_string_input(self):
        """Test that non-string inputs are handled."""
        assert is_valid_email(123) == False
        assert is_valid_email([]) == False
        assert is_valid_email({}) == False

