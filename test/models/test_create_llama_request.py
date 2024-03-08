import unittest
from src.llamastore.models.CreateLlamaRequest import CreateLlamaRequest


class TestCreateLlamaRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_create_llama_request(self):
        # Create CreateLlamaRequest class instance
        test_model = CreateLlamaRequest(
            rating=9, color="brown", age=2, name="aspernatur"
        )
        self.assertEqual(test_model.rating, 9)
        self.assertEqual(test_model.color, "brown")
        self.assertEqual(test_model.age, 2)
        self.assertEqual(test_model.name, "aspernatur")

    def test_create_llama_request_required_fields_missing(self):
        # Assert CreateLlamaRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = CreateLlamaRequest()


if __name__ == "__main__":
    unittest.main()
