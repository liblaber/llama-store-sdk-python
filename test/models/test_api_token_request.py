import unittest
from src.llamastore.models.ApiTokenRequest import ApiTokenRequest


class TestApiTokenRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_api_token_request(self):
        # Create ApiTokenRequest class instance
        test_model = ApiTokenRequest(
            password="animi",
            email="8D;W&Y{QM}{G:/^1GO\"-[#*oOUakg=U6VO'O8*;b/I[+38jJ:nn<|nUp=ZOKLu!B>h'JV4I6!B7@/,&'&+(Kh=L!L}T3yM^q@tVIc`<;.O>N_+&{GYIW[Zgr$+F^_%ax9=]DG}",
        )
        self.assertEqual(test_model.password, "animi")
        self.assertEqual(
            test_model.email,
            "8D;W&Y{QM}{G:/^1GO\"-[#*oOUakg=U6VO'O8*;b/I[+38jJ:nn<|nUp=ZOKLu!B>h'JV4I6!B7@/,&'&+(Kh=L!L}T3yM^q@tVIc`<;.O>N_+&{GYIW[Zgr$+F^_%ax9=]DG}",
        )

    def test_api_token_request_required_fields_missing(self):
        # Assert ApiTokenRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ApiTokenRequest()


if __name__ == "__main__":
    unittest.main()
