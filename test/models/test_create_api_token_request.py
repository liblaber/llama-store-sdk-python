import unittest
from src.llamastore.models.CreateApiTokenRequest import CreateApiTokenRequest


class TestCreateApiTokenRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_create_api_token_request(self):
        # Create CreateApiTokenRequest class instance
        test_model = CreateApiTokenRequest(
            password="exercitationem",
            email="I@|J+O*dvY}1HSn&]s~~;\".K##~6//:o7iR2ix?!7WP0xv{LlxU: DoEd(f)_)3Lyrh@@k!Pq=[=kTd[`3f!V<4xaS)Ie%:44L.V9%9O=J7@%+JQ?.&O2@;)MlB|jY8a}g_)ce2]7''=8krDXe>0KF,",
        )
        self.assertEqual(test_model.password, "exercitationem")
        self.assertEqual(
            test_model.email,
            "I@|J+O*dvY}1HSn&]s~~;\".K##~6//:o7iR2ix?!7WP0xv{LlxU: DoEd(f)_)3Lyrh@@k!Pq=[=kTd[`3f!V<4xaS)Ie%:44L.V9%9O=J7@%+JQ?.&O2@;)MlB|jY8a}g_)ce2]7''=8krDXe>0KF,",
        )

    def test_create_api_token_request_required_fields_missing(self):
        # Assert CreateApiTokenRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = CreateApiTokenRequest()


if __name__ == "__main__":
    unittest.main()
