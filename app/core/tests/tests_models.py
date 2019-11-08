
from django.test import TestCase
from django.contrib.auth import get_user_model


# classes for test

class ModelTest(TestCase):

    def test_create_user_with_email(self):
        email = 'hosam77@gmail.com'
        password = 'hosam7asko'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'hosam66@GMAIL.com'
        user = get_user_model().objects.create_user(email, 'hosam7asko')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'hosam7asko')

    def test_create_new_supeuser(self):
        user = get_user_model().objects.create_user(
            'hosam88@gmail.com',
            'hosam7asko'
        )
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_staff)
