import unittest
import responses
from src.llamastore.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.llamastore.services.user import User


class TestUser_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_get_user_by_email(self):
        # Mock the API response
        responses.get(
            "http://localhost:8000/user/_\\{<G@KG(xg|#8)Dg*9}gd]oTRx'(d/)Nv <nxCN|M^+Nt(4eyhq.M-3tNW`0",
            json={},
            status=200,
        )
        # call the method to test
        test_service = User("testkey")
        response = test_service.get_user_by_email(
            "_\\{<G@KG(xg|#8)Dg*9}gd]oTRx'(d/)Nv <nxCN|M^+Nt(4eyhq.M-3tNW`0"
        )
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_user_by_email_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://localhost:8000/user/SQ=.rqBE1lE@n\\&'4NX'w7\\dx?caU@Mn+X`gwymi;< ZK~ 5HQ8M\\wO}fnQZ]=obw|v9~'O&x\\\"F|$sJASv7/,g/`K`/qhG-k2nR`5%+Kfk.X~HLDb;k*FW*;k)R2YnjO\\cv`d0PbQ:R~oPE+[;+mdL1\\A,>-kBKVFr6Eb4S/{!!;\"(}Z*tUdPy3hhL\"?0>;",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = User("testkey")
            test_service.get_user_by_email()
        responses.reset(),

    @responses.activate
    def test_get_user_by_email_error_on_non_200(self):
        # Mock the API response
        responses.get(
            'http://localhost:8000/user/Yx7pH:MXuQ2:7y \\Zp6[)&g~3wpe}NJ8+5}8wB1L_>|zgBDVqx8XIQ}:\'P/DXTmuI%K)xHX%cM{|PbwG$bV=\\f&:;/pSH@3d1KDAh!Rh7-J(o(S_>S/M,CSLP]YoP?rZ`\\f!{>OKofe zyp)Zn(CKWbG})xM2f-XI08P<9_ B$nd"gy~%m3HBLYAH|[fO:P.;YH5|=xwm_R}&3tPIdk`CG*M\\BG+y,&(\\YBl#j(EFKPu-]rzbk4*THQ)z{cMyn2f|8n}S`4p@AcKf`?cCvF\\uvfEky"L$',
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = User("testkey")
            test_service.get_user_by_email(
                'Yx7pH:MXuQ2:7y \\Zp6[)&g~3wpe}NJ8+5}8wB1L_>|zgBDVqx8XIQ}:\'P/DXTmuI%K)xHX%cM{|PbwG$bV=\\f&:;/pSH@3d1KDAh!Rh7-J(o(S_>S/M,CSLP]YoP?rZ`\\f!{>OKofe zyp)Zn(CKWbG})xM2f-XI08P<9_ B$nd"gy~%m3HBLYAH|[fO:P.;YH5|=xwm_R}&3tPIdk`CG*M\\BG+y,&(\\YBl#j(EFKPu-]rzbk4*THQ)z{cMyn2f|8n}S`4p@AcKf`?cCvF\\uvfEky"L$'
            )
        responses.reset()

    @responses.activate
    def test_register_user(self):
        # Mock the API response
        responses.post("http://localhost:8000/user", json={}, status=200)
        # call the method to test
        test_service = User("testkey")
        response = test_service.register_user({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_register_user_error_on_non_200(self):
        # Mock the API response
        responses.post("http://localhost:8000/user", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = User("testkey")
            test_service.register_user({})
        responses.reset()


if __name__ == "__main__":
    unittest.main()
