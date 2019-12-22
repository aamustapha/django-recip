"""
Creates test case for app models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """
        Method tests if creating a user with valid email and passwords succeeds
        """
        email = 'amustapha@gmail.com'
        password = 'SecurePasswordWith1234Numbers'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Method to test user emaail is normalized"""
        email = "amustapha@GMAIL.COM"
        user = get_user_model().objects.create_user(
            email=email,
            password='falsepassword123'
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """
        Test creaating new user without email throws error
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None)

    def test_create_superuser(self):
        """
        Tests creation of superuser
        """

        user = get_user_model().objects.create_superuser(
            email='amustapha@hooli.ng',
            password='fake`12323'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
