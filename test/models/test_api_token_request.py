import unittest
from src.llamastore.models.ApiTokenRequest import ApiTokenRequest


class TestApiTokenRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_api_token_request(self):
        # Create ApiTokenRequest class instance
        test_model = ApiTokenRequest(
            password="assumenda",
            email="H6`D&f!qjug`00d5`Bqi[#p8.HH6M\\SyeY.F`5tyG(j_vbVMDAU:LF?5%Bv*0Q=gC!2]@2?ERr5[*7}=a(18.gF 4.Cpt1RZ8G^j34|:6zz&DvU9e}A>q\"Hw76;`?1TPtt`ArSca',ECfjZ`~4eT+@w={o%qGbopy3?",
        )
        self.assertEqual(test_model.password, "assumenda")
        self.assertEqual(
            test_model.email,
            "H6`D&f!qjug`00d5`Bqi[#p8.HH6M\\SyeY.F`5tyG(j_vbVMDAU:LF?5%Bv*0Q=gC!2]@2?ERr5[*7}=a(18.gF 4.Cpt1RZ8G^j34|:6zz&DvU9e}A>q\"Hw76;`?1TPtt`ArSca',ECfjZ`~4eT+@w={o%qGbopy3?",
        )

    def test_api_token_request_required_fields_missing(self):
        # Assert ApiTokenRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ApiTokenRequest()


if __name__ == "__main__":
    unittest.main()
