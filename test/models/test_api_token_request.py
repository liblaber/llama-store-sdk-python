import unittest
from src.llamastore.models.ApiTokenRequest import ApiTokenRequest


class TestApiTokenRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_api_token_request(self):
        # Create ApiTokenRequest class instance
        test_model = ApiTokenRequest(
            password="cum",
            email='yC[Kh>9kEVP#x+C`@Dyt!R%T~CR25 F,UzK9!2[`+X/)^"V:wK:`Y?9g^go 3Qx_Quf)fht\\M-`sWZ&MyKb>k!-2o1,JK_j\'jy>-[38DOD+Pgq?ga.A3c"j ]TCH\\x^MG0,CDoienh',
        )
        self.assertEqual(test_model.password, "cum")
        self.assertEqual(
            test_model.email,
            'yC[Kh>9kEVP#x+C`@Dyt!R%T~CR25 F,UzK9!2[`+X/)^"V:wK:`Y?9g^go 3Qx_Quf)fht\\M-`sWZ&MyKb>k!-2o1,JK_j\'jy>-[38DOD+Pgq?ga.A3c"j ]TCH\\x^MG0,CDoienh',
        )

    def test_api_token_request_required_fields_missing(self):
        # Assert ApiTokenRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ApiTokenRequest()


if __name__ == "__main__":
    unittest.main()
