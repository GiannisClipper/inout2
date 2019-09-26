from django.test import TestCase
#from django.test import Client
from rest_framework.test import APIClient
from rest_framework import status

from django.contrib.auth import get_user_model
from users import models


class PublicUsersRequestTest(TestCase):

    def test_signup_response(self):

        client = APIClient()
        res = client.get('/users/signup')
        self.assertEqual(status.HTTP_200_OK, res.status_code)
        self.assertIn(b'signup', res.content)


class PrivateUsersRequestTest(TestCase):

    def setUp(self):
        self.samples = [
            {'email': 'test@email.org', 'password': 'test1', 'name':'Anyone'},
            {'email': 'test2@email.org', 'password': 'test2', 'name': ''}
        ]

        self.client = APIClient()
        self.user, error = get_user_model().objects.create_user(**self.samples[0])
        self.client.force_authenticate(self.user)
        # self.client.force_login(self.user)

    def test_authorized_retrieve_response(self):
        res = self.client.get(f'/users/{self.user.id}/')
        self.assertEqual(status.HTTP_200_OK, res.status_code)
        self.assertIn(f'{self.user.id}'.encode(), res.content)

    def test_unauthorized_retrieve_response(self):
        res = self.client.get('/users/0/')
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, res.status_code)