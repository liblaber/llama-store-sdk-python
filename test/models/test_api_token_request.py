import unittest
from src.llamastore.models.ApiTokenRequest import ApiTokenRequest


class TestApiTokenRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_api_token_request(self):
        # Create ApiTokenRequest class instance
        test_model = ApiTokenRequest(
            password="animi",
            email="(}e8g;8rL7 |=s3T_?CH3?!vD92nTD}dI*t@5NIj.\\aR/i~`f=dtnMutbO_\\UyxIl*i~Gpq:Xg#~;a,`?fgd8>X3\\~Qi.DzW?G?;?1XjVRDZn7qo$!@[CA!EJK('0Xd{LS^6\"<0^(a^chR%6w^&ZJzjx&CK6+YA",
        )
        self.assertEqual(test_model.password, "animi")
        self.assertEqual(
            test_model.email,
            "(}e8g;8rL7 |=s3T_?CH3?!vD92nTD}dI*t@5NIj.\\aR/i~`f=dtnMutbO_\\UyxIl*i~Gpq:Xg#~;a,`?fgd8>X3\\~Qi.DzW?G?;?1XjVRDZn7qo$!@[CA!EJK('0Xd{LS^6\"<0^(a^chR%6w^&ZJzjx&CK6+YA",
        )

    def test_api_token_request_required_fields_missing(self):
        # Assert ApiTokenRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ApiTokenRequest()


if __name__ == "__main__":
    unittest.main()
