import unittest
from src.llamastore.models.Llama import Llama


class TestLlamaModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_llama(self):
        # Create Llama class instance
        test_model = Llama(id=6, rating=5, color="brown", age=7, name="omnis")
        self.assertEqual(test_model.id, 6)
        self.assertEqual(test_model.rating, 5)
        self.assertEqual(test_model.color, "brown")
        self.assertEqual(test_model.age, 7)
        self.assertEqual(test_model.name, "omnis")

    def test_llama_required_fields_missing(self):
        # Assert Llama class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = Llama()


if __name__ == "__main__":
    unittest.main()
