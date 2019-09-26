from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

from users import models


class UserModelTests(TestCase):

    def setUp(self):
        self.samples = [
            {'email': 'test@email.org', 'password': 'test1', 'name':'Anyone'},
            {'email': 'test2@email.org', 'password': 'test2', 'name': ''}
        ]

    def test_create_user(self):
        user, error = get_user_model().objects.create_user(**self.samples[0])

        self.assertEqual(user.email, self.samples[0]['email'])
        self.assertTrue(user.check_password(self.samples[0]['password']))
        self.assertEqual(user.name, self.samples[0]['name'])

    def test_create_superuser(self):
        user, error = get_user_model().objects.create_superuser(**self.samples[1])

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_email_saved_normalized(self):
        self.samples[0]['email'] = self.samples[0]['email'].upper()
        user, error = get_user_model().objects.create_user(**self.samples[0])

        self.assertEqual(
            user.email, 
            self.samples[0]['email'].split('@')[0] + '@' + 
            self.samples[0]['email'].split('@')[1].lower()
        )

    def test_email_empty_is_invalid(self):
        self.samples[0]['email'] = ''
        get_user_model().objects.create_user(**self.samples[0])

        # with self.assertRaises(ValueError):
        user, error = get_user_model().objects.create_user(**self.samples[0])
        self.assertEqual(422, error['status_code'])

    def test_email_duplicate_is_invalid(self):
        get_user_model().objects.create_user(**self.samples[0])

        # with self.assertRaises(IntegrityError):
        user, error = get_user_model().objects.create_user(**self.samples[0])
        self.assertEqual(422, error['status_code'])

    def test_user_str_representation(self):
        user, error = get_user_model().objects.create_user(**self.samples[0])

        self.assertEqual(f"{self.samples[0]['name']} ({self.samples[0]['email']})", str(user))