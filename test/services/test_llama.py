import unittest
import responses
from src.llamastore.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.llamastore.services.llama import Llama


class TestLlama_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_get_llamas(self):
        # Mock the API response
        responses.get("http://localhost:8000/llama", json={}, status=200)
        # call the method to test
        test_service = Llama("testkey")
        response = test_service.get_llamas()
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_llamas_error_on_non_200(self):
        # Mock the API response
        responses.get("http://localhost:8000/llama", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Llama("testkey")
            test_service.get_llamas()
        responses.reset()

    @responses.activate
    def test_create_llama(self):
        # Mock the API response
        responses.post("http://localhost:8000/llama", json={}, status=200)
        # call the method to test
        test_service = Llama("testkey")
        response = test_service.create_llama({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_create_llama_error_on_non_200(self):
        # Mock the API response
        responses.post("http://localhost:8000/llama", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Llama("testkey")
            test_service.create_llama({})
        responses.reset()

    @responses.activate
    def test_get_llama_by_id(self):
        # Mock the API response
        responses.get("http://localhost:8000/llama/2534355165", json={}, status=200)
        # call the method to test
        test_service = Llama("testkey")
        response = test_service.get_llama_by_id(2534355165)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_llama_by_id_required_fields_missing(self):
        # Mock the API response
        responses.get("http://localhost:8000/llama/8702382703", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Llama("testkey")
            test_service.get_llama_by_id()
        responses.reset(),

    @responses.activate
    def test_get_llama_by_id_error_on_non_200(self):
        # Mock the API response
        responses.get("http://localhost:8000/llama/6160292169", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Llama("testkey")
            test_service.get_llama_by_id(6160292169)
        responses.reset()

    @responses.activate
    def test_update_llama(self):
        # Mock the API response
        responses.put("http://localhost:8000/llama/1905854765", json={}, status=200)
        # call the method to test
        test_service = Llama("testkey")
        response = test_service.update_llama({}, 1905854765)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_update_llama_required_fields_missing(self):
        # Mock the API response
        responses.put("http://localhost:8000/llama/1538563307", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Llama("testkey")
            test_service.update_llama()
        responses.reset(),

    @responses.activate
    def test_update_llama_error_on_non_200(self):
        # Mock the API response
        responses.put("http://localhost:8000/llama/2867398589", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Llama("testkey")
            test_service.update_llama({}, 2867398589)
        responses.reset()

    @responses.activate
    def test_delete_llama(self):
        # Mock the API response
        responses.delete("http://localhost:8000/llama/7001320851", json={}, status=200)
        # call the method to test
        test_service = Llama("testkey")
        response = test_service.delete_llama(7001320851)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_llama_required_fields_missing(self):
        # Mock the API response
        responses.delete("http://localhost:8000/llama/3450004469", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Llama("testkey")
            test_service.delete_llama()
        responses.reset(),

    @responses.activate
    def test_delete_llama_error_on_non_200(self):
        # Mock the API response
        responses.delete("http://localhost:8000/llama/5838396433", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Llama("testkey")
            test_service.delete_llama(5838396433)
        responses.reset()


if __name__ == "__main__":
    unittest.main()
