import unittest
from src.llamastore.models.Llama import Llama


class TestLlamaModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_llama(self):
        # Create Llama class instance
        test_model = Llama(id=2, rating=9, color="brown", age=6, name="quaerat")
        self.assertEqual(test_model.id, 2)
        self.assertEqual(test_model.rating, 9)
        self.assertEqual(test_model.color, "brown")
        self.assertEqual(test_model.age, 6)
        self.assertEqual(test_model.name, "quaerat")

    def test_llama_required_fields_missing(self):
        # Assert Llama class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = Llama()


if __name__ == "__main__":
    unittest.main()
