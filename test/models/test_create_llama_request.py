import unittest
from src.llamastore.models.CreateLlamaRequest import CreateLlamaRequest


class TestCreateLlamaRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_create_llama_request(self):
        # Create CreateLlamaRequest class instance
        test_model = CreateLlamaRequest(rating=1, color="brown", age=4, name="ullam")
        self.assertEqual(test_model.rating, 1)
        self.assertEqual(test_model.color, "brown")
        self.assertEqual(test_model.age, 4)
        self.assertEqual(test_model.name, "ullam")

    def test_create_llama_request_required_fields_missing(self):
        # Assert CreateLlamaRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = CreateLlamaRequest()


if __name__ == "__main__":
    unittest.main()
