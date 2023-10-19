import unittest
from src.llamastore.models.ApiTokenRequest import ApiTokenRequest


class TestApiTokenRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_api_token_request(self):
        # Create ApiTokenRequest class instance
        test_model = ApiTokenRequest(
            password="perferendis",
            email="CT\\lYzFc2`6S67D?UR@!M`$|XU~2rgQLSs@h(a=& X%yXa7GXK%Bw#2 gtqw#*6 3%g7Nmq!W+5CK)Tp06X,QxS=^-5tsV=X TO8~;J7(f7[|QZNv~W.RBSFFLg=9~(|L}=yqBs|ux8&",
        )
        self.assertEqual(test_model.password, "perferendis")
        self.assertEqual(
            test_model.email,
            "CT\\lYzFc2`6S67D?UR@!M`$|XU~2rgQLSs@h(a=& X%yXa7GXK%Bw#2 gtqw#*6 3%g7Nmq!W+5CK)Tp06X,QxS=^-5tsV=X TO8~;J7(f7[|QZNv~W.RBSFFLg=9~(|L}=yqBs|ux8&",
        )

    def test_api_token_request_required_fields_missing(self):
        # Assert ApiTokenRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ApiTokenRequest()


if __name__ == "__main__":
    unittest.main()
