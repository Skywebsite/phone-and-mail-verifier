"""
Unit tests for phone number validation.
"""

import pytest
from email_phone_validator.phone import is_valid_phone


class TestPhoneValidation:
    """Test cases for phone number validation."""
    
    def test_valid_indian_phones(self):
        """Test valid Indian phone numbers."""
        valid_indian_phones = [
            "9876543210",
            "+919876543210",
            "919876543210",
            "09876543210",
        ]
        
        for phone in valid_indian_phones:
            assert is_valid_phone(phone, "IN") == True, f"{phone} should be valid for India"
    
    def test_invalid_indian_phones(self):
        """Test invalid Indian phone numbers."""
        invalid_indian_phones = [
            "12345",
            "123456789",
            "98765432101",  # Too long
            "abc1234567",
            "",
            " ",
        ]
        
        for phone in invalid_indian_phones:
            assert is_valid_phone(phone, "IN") == False, f"{phone} should be invalid for India"
    
    def test_valid_us_phones(self):
        """Test valid US phone numbers."""
        valid_us_phones = [
            "+12025551234",
            "2025551234",
            "(202) 555-1234",
        ]
        
        for phone in valid_us_phones:
            assert is_valid_phone(phone, "US") == True, f"{phone} should be valid for US"
    
    def test_default_country(self):
        """Test that default country is India."""
        assert is_valid_phone("9876543210") == True
        assert is_valid_phone("12345") == False
    
    def test_non_string_input(self):
        """Test that non-string inputs are handled."""
        assert is_valid_phone(123) == False
        assert is_valid_phone([]) == False
        assert is_valid_phone(None) == False
    
    def test_empty_string(self):
        """Test that empty strings are handled."""
        assert is_valid_phone("") == False
        assert is_valid_phone("   ") == False

