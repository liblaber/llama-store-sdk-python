import unittest
from src.llamastore.models.LlamaId import LlamaId


class TestLlamaIdModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_llama_id(self):
        # Create LlamaId class instance
        test_model = LlamaId(id=4)
        self.assertEqual(test_model.id, 4)

    def test_llama_id_required_fields_missing(self):
        # Assert LlamaId class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = LlamaId()


if __name__ == "__main__":
    unittest.main()
