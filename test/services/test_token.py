import unittest
import responses
from src.llamastore.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.llamastore.services.token import Token


class TestToken_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_create_api_token(self):
        # Mock the API response
        responses.post("http://localhost:8000/token", json={}, status=200)
        # call the method to test
        test_service = Token("testkey")
        response = test_service.create_api_token({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_create_api_token_error_on_non_200(self):
        # Mock the API response
        responses.post("http://localhost:8000/token", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Token("testkey")
            test_service.create_api_token({})
        responses.reset()


if __name__ == "__main__":
    unittest.main()
