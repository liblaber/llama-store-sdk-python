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
            "http://localhost:8000/llama/6194571739/picture", json={}, status=200
        )
        # call the method to test
        test_service = LlamaPicture("testkey")
        response = test_service.get_llama_picture_by_llama_id(6194571739)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_llama_picture_by_llama_id_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://localhost:8000/llama/1772567376/picture", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = LlamaPicture("testkey")
            test_service.get_llama_picture_by_llama_id()
        responses.reset(),

    @responses.activate
    def test_get_llama_picture_by_llama_id_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://localhost:8000/llama/3830555727/picture", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = LlamaPicture("testkey")
            test_service.get_llama_picture_by_llama_id(3830555727)
        responses.reset()

    @responses.activate
    def test_create_llama_picture(self):
        # Mock the API response
        responses.post(
            "http://localhost:8000/llama/9948219370/picture", json={}, status=200
        )
        # call the method to test
        test_service = LlamaPicture("testkey")
        response = test_service.create_llama_picture(9948219370, {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_create_llama_picture_required_fields_missing(self):
        # Mock the API response
        responses.post(
            "http://localhost:8000/llama/9238751080/picture", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = LlamaPicture("testkey")
            test_service.create_llama_picture()
        responses.reset(),

    @responses.activate
    def test_create_llama_picture_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "http://localhost:8000/llama/6967077343/picture", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = LlamaPicture("testkey")
            test_service.create_llama_picture(6967077343, {})
        responses.reset()

    @responses.activate
    def test_update_llama_picture(self):
        # Mock the API response
        responses.put(
            "http://localhost:8000/llama/4760414610/picture", json={}, status=200
        )
        # call the method to test
        test_service = LlamaPicture("testkey")
        response = test_service.update_llama_picture(4760414610, {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_update_llama_picture_required_fields_missing(self):
        # Mock the API response
        responses.put(
            "http://localhost:8000/llama/2236088313/picture", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = LlamaPicture("testkey")
            test_service.update_llama_picture()
        responses.reset(),

    @responses.activate
    def test_update_llama_picture_error_on_non_200(self):
        # Mock the API response
        responses.put(
            "http://localhost:8000/llama/4191385005/picture", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = LlamaPicture("testkey")
            test_service.update_llama_picture(4191385005, {})
        responses.reset()

    @responses.activate
    def test_delete_llama_picture(self):
        # Mock the API response
        responses.delete(
            "http://localhost:8000/llama/8921575143/picture", json={}, status=200
        )
        # call the method to test
        test_service = LlamaPicture("testkey")
        response = test_service.delete_llama_picture(8921575143)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_llama_picture_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "http://localhost:8000/llama/9779154069/picture", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = LlamaPicture("testkey")
            test_service.delete_llama_picture()
        responses.reset(),

    @responses.activate
    def test_delete_llama_picture_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "http://localhost:8000/llama/9019421502/picture", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = LlamaPicture("testkey")
            test_service.delete_llama_picture(9019421502)
        responses.reset()


if __name__ == "__main__":
    unittest.main()
