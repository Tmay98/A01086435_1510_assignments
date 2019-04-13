from unittest import TestCase
from password_validator import password_validator


class TestPassword_validator(TestCase):
    def test_password_validator(self):
        self.assertTrue(password_validator('Abdcsd123'))

    def test_no_uppercase(self):
        self.assertFalse(password_validator('crocodile3'))

    def test_no_number(self):
        self.assertFalse(password_validator('DdsfdsFFDSffS'))

    def test_not_8_characters_long(self):
        self.assertFalse(password_validator('AbC123'))
