from django.contrib.auth import get_user_model
from django.test import TestCase


class UserTest(TestCase):
    def test_create_user(self):
        user = get_user_model().objects.create_user(
            email='coninggu@example.com',
            username='coninggu',
            password='testpassword12!@#',
        )
        self.assertEqual(user.email, 'coninggu@example.com')
        self.assertEqual(user.username, 'coninggu')
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            email='superuser@example.com',
            username='superuser',
            password='testpassword12!@#',
        )
        self.assertEqual(user.email, 'superuser@example.com')
        self.assertEqual(user.username, 'superuser')
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_active)