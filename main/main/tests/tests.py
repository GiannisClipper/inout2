from django.test import TestCase
from django.test import Client
from rest_framework import status

from main.constants import WELCOME, COPYRIGHT


class RootRequestTest(TestCase):

    def test_root_response(self):
        client = Client()
        res = client.get('/')
        
        self.assertEqual(status.HTTP_200_OK, res.status_code)
        self.assertIn(WELCOME.encode(), res.content)
        self.assertIn(COPYRIGHT.encode(), res.content)