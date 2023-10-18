import unittest
from src.llamastore.models.ApiTokenRequest import ApiTokenRequest


class TestApiTokenRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_api_token_request(self):
        # Create ApiTokenRequest class instance
        test_model = ApiTokenRequest(
            password="sit",
            email='xnSi0\\f<DMB0}V-4*)5[u!GVl_UhJRBn`tQ+#/^x}t{J6fx9oXr#j0R_RR-cq]b_p]E\'K"N@iA0x>%wC(k>d|g@^;X.Cp?"{w^U}`Z,9qCZvU;+.P8>L.v_J%-DGBJ8BHs=8;oMhf}fM4%EH|_rZ(>nG(2rVdnX*+yQSdK{?Q43JABUN.4VcHDiO/oq8Qo]vD0/<b$e1, >_yeu3xnV *wtD!6~,bTUjH1e&vUk3z"xqSW!d_2-JH6jxkM]hQr]<T:6L:[NQ<0!F',
        )
        self.assertEqual(test_model.password, "sit")
        self.assertEqual(
            test_model.email,
            'xnSi0\\f<DMB0}V-4*)5[u!GVl_UhJRBn`tQ+#/^x}t{J6fx9oXr#j0R_RR-cq]b_p]E\'K"N@iA0x>%wC(k>d|g@^;X.Cp?"{w^U}`Z,9qCZvU;+.P8>L.v_J%-DGBJ8BHs=8;oMhf}fM4%EH|_rZ(>nG(2rVdnX*+yQSdK{?Q43JABUN.4VcHDiO/oq8Qo]vD0/<b$e1, >_yeu3xnV *wtD!6~,bTUjH1e&vUk3z"xqSW!d_2-JH6jxkM]hQr]<T:6L:[NQ<0!F',
        )

    def test_api_token_request_required_fields_missing(self):
        # Assert ApiTokenRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ApiTokenRequest()


if __name__ == "__main__":
    unittest.main()
