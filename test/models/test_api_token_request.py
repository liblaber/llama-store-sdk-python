import unittest
from src.llamastore.models.ApiTokenRequest import ApiTokenRequest


class TestApiTokenRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_api_token_request(self):
        # Create ApiTokenRequest class instance
        test_model = ApiTokenRequest(
            password="ut",
            email="'voiavzL\\U_4&F%2k`7|aNCUFiKl<F$Ew5iAR]Rf8S[b)AH(p\\\\xRY8p_.f@=MkVu OA)!Cx?[~7OmNHQ5D;a\"pM3TqjBN-&}#zC[)AAv8cP0./CRFe:-1O<G=Lv;8,m\\|3A(c+.%)*6(o7.u#UuZ>:Km~`",
        )
        self.assertEqual(test_model.password, "ut")
        self.assertEqual(
            test_model.email,
            "'voiavzL\\U_4&F%2k`7|aNCUFiKl<F$Ew5iAR]Rf8S[b)AH(p\\\\xRY8p_.f@=MkVu OA)!Cx?[~7OmNHQ5D;a\"pM3TqjBN-&}#zC[)AAv8cP0./CRFe:-1O<G=Lv;8,m\\|3A(c+.%)*6(o7.u#UuZ>:Km~`",
        )

    def test_api_token_request_required_fields_missing(self):
        # Assert ApiTokenRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ApiTokenRequest()


if __name__ == "__main__":
    unittest.main()
