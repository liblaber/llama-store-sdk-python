import unittest
from src.llamastore.models.ApiToken import ApiToken


class TestApiTokenModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_api_token(self):
        # Create ApiToken class instance
        test_model = ApiToken(access_token="distinctio", token_type="molestiae")
        self.assertEqual(test_model.access_token, "distinctio")
        self.assertEqual(test_model.token_type, "molestiae")

    def test_api_token_required_fields_missing(self):
        # Assert ApiToken class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ApiToken()


if __name__ == "__main__":
    unittest.main()
