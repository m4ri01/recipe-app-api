"""
Test model function
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """test models"""

    def test_create_user_with_email(self):
        """
        test creating a user with email address
        """

        email = "example@example.com"
        password = "12345678"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_normalize_email(self):
        """Test normalize email"""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@example.COM', 'TEST3@example.com'],
            ['tesT4@EXAMPLE.COM', 'tesT4@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(
                email=email,
                password="12345678"
            )

            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test if a new user create without email will raise an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email="", password="123")

    def test_new_super_user(self):
        """Test creating super user feature"""
        user = get_user_model().objects.create_superuser(
            email="test@test.example",
            password="12345678"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
