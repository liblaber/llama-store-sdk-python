import unittest
from src.llamastore.models.LlamaCreate import LlamaCreate


class TestLlamaCreateModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_llama_create(self):
        # Create LlamaCreate class instance
        test_model = LlamaCreate(rating=4, color="brown", age=2, name="ex")
        self.assertEqual(test_model.rating, 4)
        self.assertEqual(test_model.color, "brown")
        self.assertEqual(test_model.age, 2)
        self.assertEqual(test_model.name, "ex")

    def test_llama_create_required_fields_missing(self):
        # Assert LlamaCreate class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = LlamaCreate()


if __name__ == "__main__":
    unittest.main()
