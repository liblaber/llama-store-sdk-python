import unittest
from src.llamastore.models.CreateApiTokenRequest import CreateApiTokenRequest


class TestCreateApiTokenRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_create_api_token_request(self):
        # Create CreateApiTokenRequest class instance
        test_model = CreateApiTokenRequest(
            password="nostrum",
            email='msE]{d^n(^5@@E_x3PVv|n`p#@.}}-6%R<q!9xW0Go;aKL,X5SAf@<WLa\\j1"+kJ^h9c`>On9E"s2s_fu_#HTnxtv@2^Oy&k,$?./h#ka8I0V@4f$uRTDcqq,j7I3pU5giC8Z#kb^XukpVR/0y%@peu.X:\\XDk 2l$Y',
        )
        self.assertEqual(test_model.password, "nostrum")
        self.assertEqual(
            test_model.email,
            'msE]{d^n(^5@@E_x3PVv|n`p#@.}}-6%R<q!9xW0Go;aKL,X5SAf@<WLa\\j1"+kJ^h9c`>On9E"s2s_fu_#HTnxtv@2^Oy&k,$?./h#ka8I0V@4f$uRTDcqq,j7I3pU5giC8Z#kb^XukpVR/0y%@peu.X:\\XDk 2l$Y',
        )

    def test_create_api_token_request_required_fields_missing(self):
        # Assert CreateApiTokenRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = CreateApiTokenRequest()


if __name__ == "__main__":
    unittest.main()
