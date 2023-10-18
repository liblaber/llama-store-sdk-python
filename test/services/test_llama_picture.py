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
            "http://localhost:8000/llama/7007429338/picture", json={}, status=200
        )
        # call the method to test
        test_service = LlamaPicture("testkey")
        response = test_service.get_llama_picture_by_llama_id(7007429338)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_llama_picture_by_llama_id_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://localhost:8000/llama/5159261988/picture", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = LlamaPicture("testkey")
            test_service.get_llama_picture_by_llama_id()
        responses.reset(),

    @responses.activate
    def test_get_llama_picture_by_llama_id_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://localhost:8000/llama/4357496944/picture", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = LlamaPicture("testkey")
            test_service.get_llama_picture_by_llama_id(4357496944)
        responses.reset()

    @responses.activate
    def test_create_llama_picture(self):
        # Mock the API response
        responses.post(
            "http://localhost:8000/llama/6725298303/picture", json={}, status=200
        )
        # call the method to test
        test_service = LlamaPicture("testkey")
        response = test_service.create_llama_picture(6725298303, {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_create_llama_picture_required_fields_missing(self):
        # Mock the API response
        responses.post(
            "http://localhost:8000/llama/4919441313/picture", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = LlamaPicture("testkey")
            test_service.create_llama_picture()
        responses.reset(),

    @responses.activate
    def test_create_llama_picture_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "http://localhost:8000/llama/4134906336/picture", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = LlamaPicture("testkey")
            test_service.create_llama_picture(4134906336, {})
        responses.reset()

    @responses.activate
    def test_update_llama_picture(self):
        # Mock the API response
        responses.put(
            "http://localhost:8000/llama/1238489956/picture", json={}, status=200
        )
        # call the method to test
        test_service = LlamaPicture("testkey")
        response = test_service.update_llama_picture(1238489956, {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_update_llama_picture_required_fields_missing(self):
        # Mock the API response
        responses.put(
            "http://localhost:8000/llama/6756279896/picture", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = LlamaPicture("testkey")
            test_service.update_llama_picture()
        responses.reset(),

    @responses.activate
    def test_update_llama_picture_error_on_non_200(self):
        # Mock the API response
        responses.put(
            "http://localhost:8000/llama/3901827203/picture", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = LlamaPicture("testkey")
            test_service.update_llama_picture(3901827203, {})
        responses.reset()

    @responses.activate
    def test_delete_llama_picture(self):
        # Mock the API response
        responses.delete(
            "http://localhost:8000/llama/7014148955/picture", json={}, status=200
        )
        # call the method to test
        test_service = LlamaPicture("testkey")
        response = test_service.delete_llama_picture(7014148955)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_llama_picture_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "http://localhost:8000/llama/9582090347/picture", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = LlamaPicture("testkey")
            test_service.delete_llama_picture()
        responses.reset(),

    @responses.activate
    def test_delete_llama_picture_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "http://localhost:8000/llama/6559219567/picture", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = LlamaPicture("testkey")
            test_service.delete_llama_picture(6559219567)
        responses.reset()


if __name__ == "__main__":
    unittest.main()
