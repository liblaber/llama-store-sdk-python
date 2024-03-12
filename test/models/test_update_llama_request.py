import unittest
from src.llamastore.models.UpdateLlamaRequest import UpdateLlamaRequest


class TestUpdateLlamaRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_update_llama_request(self):
        # Create UpdateLlamaRequest class instance
        test_model = UpdateLlamaRequest(
            rating=7, color="brown", age=5, name="voluptates"
        )
        self.assertEqual(test_model.rating, 7)
        self.assertEqual(test_model.color, "brown")
        self.assertEqual(test_model.age, 5)
        self.assertEqual(test_model.name, "voluptates")

    def test_update_llama_request_required_fields_missing(self):
        # Assert UpdateLlamaRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UpdateLlamaRequest()


if __name__ == "__main__":
    unittest.main()
