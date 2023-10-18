import unittest
from src.llamastore.models.ApiTokenRequest import ApiTokenRequest


class TestApiTokenRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_api_token_request(self):
        # Create ApiTokenRequest class instance
        test_model = ApiTokenRequest(
            password="aliquid",
            email="w1TCnq`wH1cY9/Mf2Xskruo ohnoAy8hHV*v(xohZT}O'm^H=dC=;C&;}av(&(<<jh@#x@c0su=B8ovA4cm~n~y9Zl`+~Vk|ce'W=Dmp}xL,-NiUv,8{6YH#'q9T>.nUV\\oeuIbjV KF7.QCx'mzu|4~tL-d?]y`jAWoGd[X8\\Y_6bKnO",
        )
        self.assertEqual(test_model.password, "aliquid")
        self.assertEqual(
            test_model.email,
            "w1TCnq`wH1cY9/Mf2Xskruo ohnoAy8hHV*v(xohZT}O'm^H=dC=;C&;}av(&(<<jh@#x@c0su=B8ovA4cm~n~y9Zl`+~Vk|ce'W=Dmp}xL,-NiUv,8{6YH#'q9T>.nUV\\oeuIbjV KF7.QCx'mzu|4~tL-d?]y`jAWoGd[X8\\Y_6bKnO",
        )

    def test_api_token_request_required_fields_missing(self):
        # Assert ApiTokenRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ApiTokenRequest()


if __name__ == "__main__":
    unittest.main()
