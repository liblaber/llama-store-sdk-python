import unittest
import responses
from src.llamastore.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.llamastore.services.llama_picture import LlamaPicture


class TestLlamaPicture_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_get_llama_picture_by_llama_id(self):
        # Mock the API response
        responses.get(
            "http://localhost:8000/llama/8469572921/picture", json={}, status=200
        )
        # call the method to test
        test_service = LlamaPicture("testkey")
        response = test_service.get_llama_picture_by_llama_id(8469572921)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_llama_picture_by_llama_id_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://localhost:8000/llama/2269954871/picture", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = LlamaPicture("testkey")
            test_service.get_llama_picture_by_llama_id()
        responses.reset(),

    @responses.activate
    def test_get_llama_picture_by_llama_id_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://localhost:8000/llama/5321408146/picture", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = LlamaPicture("testkey")
            test_service.get_llama_picture_by_llama_id(5321408146)
        responses.reset()

    @responses.activate
    def test_create_llama_picture(self):
        # Mock the API response
        responses.post(
            "http://localhost:8000/llama/9676209771/picture", json={}, status=200
        )
        # call the method to test
        test_service = LlamaPicture("testkey")
        response = test_service.create_llama_picture(9676209771, {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_create_llama_picture_required_fields_missing(self):
        # Mock the API response
        responses.post(
            "http://localhost:8000/llama/6386457618/picture", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = LlamaPicture("testkey")
            test_service.create_llama_picture()
        responses.reset(),

    @responses.activate
    def test_create_llama_picture_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "http://localhost:8000/llama/8494856098/picture", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = LlamaPicture("testkey")
            test_service.create_llama_picture(8494856098, {})
        responses.reset()

    @responses.activate
    def test_update_llama_picture(self):
        # Mock the API response
        responses.put(
            "http://localhost:8000/llama/4958806577/picture", json={}, status=200
        )
        # call the method to test
        test_service = LlamaPicture("testkey")
        response = test_service.update_llama_picture(4958806577, {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_update_llama_picture_required_fields_missing(self):
        # Mock the API response
        responses.put(
            "http://localhost:8000/llama/6724273776/picture", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = LlamaPicture("testkey")
            test_service.update_llama_picture()
        responses.reset(),

    @responses.activate
    def test_update_llama_picture_error_on_non_200(self):
        # Mock the API response
        responses.put(
            "http://localhost:8000/llama/4213041586/picture", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = LlamaPicture("testkey")
            test_service.update_llama_picture(4213041586, {})
        responses.reset()

    @responses.activate
    def test_delete_llama_picture(self):
        # Mock the API response
        responses.delete(
            "http://localhost:8000/llama/9513293586/picture", json={}, status=200
        )
        # call the method to test
        test_service = LlamaPicture("testkey")
        response = test_service.delete_llama_picture(9513293586)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_llama_picture_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "http://localhost:8000/llama/7873283861/picture", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = LlamaPicture("testkey")
            test_service.delete_llama_picture()
        responses.reset(),

    @responses.activate
    def test_delete_llama_picture_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "http://localhost:8000/llama/9411319774/picture", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = LlamaPicture("testkey")
            test_service.delete_llama_picture(9411319774)
        responses.reset()


if __name__ == "__main__":
    unittest.main()
