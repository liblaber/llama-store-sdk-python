import unittest
from src.llamastore.models.UpdateLlamaRequest import UpdateLlamaRequest


class TestUpdateLlamaRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_update_llama_request(self):
        # Create UpdateLlamaRequest class instance
        test_model = UpdateLlamaRequest(
            rating=8, color="brown", age=1, name="perspiciatis"
        )
        self.assertEqual(test_model.rating, 8)
        self.assertEqual(test_model.color, "brown")
        self.assertEqual(test_model.age, 1)
        self.assertEqual(test_model.name, "perspiciatis")

    def test_update_llama_request_required_fields_missing(self):
        # Assert UpdateLlamaRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UpdateLlamaRequest()


if __name__ == "__main__":
    unittest.main()
