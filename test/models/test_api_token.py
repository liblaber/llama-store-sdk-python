import unittest
from src.llamastore.models.ApiToken import ApiToken


class TestApiTokenModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_api_token(self):
        # Create ApiToken class instance
        test_model = ApiToken(access_token="voluptate", token_type="alias")
        self.assertEqual(test_model.access_token, "voluptate")
        self.assertEqual(test_model.token_type, "alias")

    def test_api_token_required_fields_missing(self):
        # Assert ApiToken class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ApiToken()


if __name__ == "__main__":
    unittest.main()
