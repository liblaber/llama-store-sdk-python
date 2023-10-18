import unittest
from src.llamastore.models.LlamaCreate import LlamaCreate


class TestLlamaCreateModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_llama_create(self):
        # Create LlamaCreate class instance
        test_model = LlamaCreate(rating=6, color="brown", age=5, name="quae")
        self.assertEqual(test_model.rating, 6)
        self.assertEqual(test_model.color, "brown")
        self.assertEqual(test_model.age, 5)
        self.assertEqual(test_model.name, "quae")

    def test_llama_create_required_fields_missing(self):
        # Assert LlamaCreate class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = LlamaCreate()


if __name__ == "__main__":
    unittest.main()
