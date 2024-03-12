import unittest
import responses
from src.llamastore.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.llamastore.services.llama_picture import LlamaPicture
from src.llamastore.hooks.hook import CustomHook


class TestLlamaPicture_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_get_llama_picture_by_llama_id(self):
        # Mock the API response
        responses.get(
            "http://localhost:8080/llama/5326915966/picture", json={}, status=200
        )
        # call the method to test
        test_service = LlamaPicture("testkey")
        response = test_service.get_llama_picture_by_llama_id(5326915966)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_llama_picture_by_llama_id_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://localhost:8080/llama/6283376734/picture", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = LlamaPicture("testkey")
            test_service.get_llama_picture_by_llama_id()
        responses.reset(),

    @responses.activate
    def test_get_llama_picture_by_llama_id_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://localhost:8080/llama/2623353000/picture", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = LlamaPicture("testkey")
            test_service.get_llama_picture_by_llama_id(2623353000)
        responses.reset()

    @responses.activate
    def test_create_llama_picture(self):
        # Mock the API response
        responses.post(
            "http://localhost:8080/llama/2491224511/picture", json={}, status=200
        )
        # call the method to test
        test_service = LlamaPicture("testkey")
        response = test_service.create_llama_picture(2491224511, {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_create_llama_picture_required_fields_missing(self):
        # Mock the API response
        responses.post(
            "http://localhost:8080/llama/8606858946/picture", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = LlamaPicture("testkey")
            test_service.create_llama_picture()
        responses.reset(),

    @responses.activate
    def test_create_llama_picture_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "http://localhost:8080/llama/2373629239/picture", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = LlamaPicture("testkey")
            test_service.create_llama_picture(2373629239, {})
        responses.reset()

    @responses.activate
    def test_update_llama_picture(self):
        # Mock the API response
        responses.put(
            "http://localhost:8080/llama/8417020818/picture", json={}, status=200
        )
        # call the method to test
        test_service = LlamaPicture("testkey")
        response = test_service.update_llama_picture(8417020818, {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_update_llama_picture_required_fields_missing(self):
        # Mock the API response
        responses.put(
            "http://localhost:8080/llama/9045264244/picture", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = LlamaPicture("testkey")
            test_service.update_llama_picture()
        responses.reset(),

    @responses.activate
    def test_update_llama_picture_error_on_non_200(self):
        # Mock the API response
        responses.put(
            "http://localhost:8080/llama/3780574656/picture", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = LlamaPicture("testkey")
            test_service.update_llama_picture(3780574656, {})
        responses.reset()

    @responses.activate
    def test_delete_llama_picture(self):
        # Mock the API response
        responses.delete(
            "http://localhost:8080/llama/4937061895/picture", json={}, status=200
        )
        # call the method to test
        test_service = LlamaPicture("testkey")
        response = test_service.delete_llama_picture(4937061895)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_llama_picture_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "http://localhost:8080/llama/6501543652/picture", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = LlamaPicture("testkey")
            test_service.delete_llama_picture()
        responses.reset(),

    @responses.activate
    def test_delete_llama_picture_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "http://localhost:8080/llama/9966467699/picture", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = LlamaPicture("testkey")
            test_service.delete_llama_picture(9966467699)
        responses.reset()


if __name__ == "__main__":
    unittest.main()
