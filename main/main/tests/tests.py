from django.test import TestCase
from django.test import Client

from main.constants import WELCOME, COPYRIGHT

class RootRequestTest(TestCase):

    def test_root_response(self):

        client = Client()
        res = client.get('/')
        self.assertIn(WELCOME.encode(), res.content)
        self.assertIn(COPYRIGHT.encode(), res.content)

