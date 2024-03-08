from django.test import TestCase, override_settings
from django.test.client import Client
from http import HTTPStatus
# Create your tests here.

class TestIPSMiddleware(TestCase):
    def setUP(self):
        self.client = Client()
    
    @override_settings(BLOCKED_IPS=None)
    def test_request_successful_with_blockedIPS(self):
        responce = self.client.get('/')
        self.assertEqual(responce.status_code, HTTPStatus.OK) # HTTPStatus.OK or 200