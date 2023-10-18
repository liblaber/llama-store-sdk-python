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
            "http://localhost:8000/llama/8812109834/picture", json={}, status=200
        )
        # call the method to test
        test_service = LlamaPicture("testkey")
        response = test_service.get_llama_picture_by_llama_id(8812109834)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_llama_picture_by_llama_id_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://localhost:8000/llama/1153432959/picture", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = LlamaPicture("testkey")
            test_service.get_llama_picture_by_llama_id()
        responses.reset(),

    @responses.activate
    def test_get_llama_picture_by_llama_id_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://localhost:8000/llama/5922537141/picture", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = LlamaPicture("testkey")
            test_service.get_llama_picture_by_llama_id(5922537141)
        responses.reset()

    @responses.activate
    def test_create_llama_picture(self):
        # Mock the API response
        responses.post(
            "http://localhost:8000/llama/5625093984/picture", json={}, status=200
        )
        # call the method to test
        test_service = LlamaPicture("testkey")
        response = test_service.create_llama_picture(5625093984, {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_create_llama_picture_required_fields_missing(self):
        # Mock the API response
        responses.post(
            "http://localhost:8000/llama/7063736764/picture", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = LlamaPicture("testkey")
            test_service.create_llama_picture()
        responses.reset(),

    @responses.activate
    def test_create_llama_picture_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "http://localhost:8000/llama/7665988791/picture", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = LlamaPicture("testkey")
            test_service.create_llama_picture(7665988791, {})
        responses.reset()

    @responses.activate
    def test_update_llama_picture(self):
        # Mock the API response
        responses.put(
            "http://localhost:8000/llama/4759892190/picture", json={}, status=200
        )
        # call the method to test
        test_service = LlamaPicture("testkey")
        response = test_service.update_llama_picture(4759892190, {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_update_llama_picture_required_fields_missing(self):
        # Mock the API response
        responses.put(
            "http://localhost:8000/llama/8963328117/picture", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = LlamaPicture("testkey")
            test_service.update_llama_picture()
        responses.reset(),

    @responses.activate
    def test_update_llama_picture_error_on_non_200(self):
        # Mock the API response
        responses.put(
            "http://localhost:8000/llama/4670686801/picture", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = LlamaPicture("testkey")
            test_service.update_llama_picture(4670686801, {})
        responses.reset()

    @responses.activate
    def test_delete_llama_picture(self):
        # Mock the API response
        responses.delete(
            "http://localhost:8000/llama/5362285801/picture", json={}, status=200
        )
        # call the method to test
        test_service = LlamaPicture("testkey")
        response = test_service.delete_llama_picture(5362285801)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_llama_picture_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "http://localhost:8000/llama/9811918532/picture", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = LlamaPicture("testkey")
            test_service.delete_llama_picture()
        responses.reset(),

    @responses.activate
    def test_delete_llama_picture_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "http://localhost:8000/llama/2153248509/picture", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = LlamaPicture("testkey")
            test_service.delete_llama_picture(2153248509)
        responses.reset()


if __name__ == "__main__":
    unittest.main()
