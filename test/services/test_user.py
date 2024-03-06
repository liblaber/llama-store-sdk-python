import unittest
import responses
from src.llamastore.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.llamastore.services.user import User
from src.llamastore.hooks.hook import CustomHook


class TestUser_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_get_user_by_email(self):
        # Mock the API response
        responses.get(
            "http://localhost:8080/user/?<|!MyiusKc|gA+7=~A-6v~-=\\u8<+,PGiCo\"@wy'U-<[]J)1I8e1^YM~?>Sn1@v ^e[RtssO1ZWvA'l&P>oq]=t?N##M_P':E4S>$@>ob(Ud^SrW.N3!-xFeqjw5kJBcf&y:_^aIQz@u5Z",
            json={},
            status=200,
        )
        # call the method to test
        test_service = User("testkey")
        response = test_service.get_user_by_email(
            "?<|!MyiusKc|gA+7=~A-6v~-=\\u8<+,PGiCo\"@wy'U-<[]J)1I8e1^YM~?>Sn1@v ^e[RtssO1ZWvA'l&P>oq]=t?N##M_P':E4S>$@>ob(Ud^SrW.N3!-xFeqjw5kJBcf&y:_^aIQz@u5Z"
        )
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_user_by_email_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://localhost:8080/user/X{{4p} 3=/CCE;tb e%8E#4,&LgP8C~XK{3s8Jo_CXWE&L8Y\\AUI*Fo47R`<h+I!oT>_$5g'<8cm3Qj#:z@?%e0mmX$C^6?+K~whr?2[c _ZIm0gpcn:iN^,)h<9F|c<;9e:\"6elj,bR)`]3s5=WFZge^e|+|.qb}\\ Slpd$R)*^fypq.2N[8, rzpkARlrytlQlwS>i",
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
            "http://localhost:8080/user/HF};K@PNG{W|1SK_ip[c+8'xC;tO|zV^<q3P1zhyc+i_Vn;B~:CQwKtv}^ex7qUo6D &Zz~_0YPu\\7$?HI_o_DIi^S'1,WY[+b N?gH.jKG:6#u!D Zupdiv&bMV~ 7!!9#D1/vNaM!zDdBW~^rmD7S%~d`*JPyD,7a$QYD~jIVH{Fdlz#iVt(jJJ$l \"ECfXe",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = User("testkey")
            test_service.get_user_by_email(
                "HF};K@PNG{W|1SK_ip[c+8'xC;tO|zV^<q3P1zhyc+i_Vn;B~:CQwKtv}^ex7qUo6D &Zz~_0YPu\\7$?HI_o_DIi^S'1,WY[+b N?gH.jKG:6#u!D Zupdiv&bMV~ 7!!9#D1/vNaM!zDdBW~^rmD7S%~d`*JPyD,7a$QYD~jIVH{Fdlz#iVt(jJJ$l \"ECfXe"
            )
        responses.reset()

    @responses.activate
    def test_register_user(self):
        # Mock the API response
        responses.post("http://localhost:8080/user", json={}, status=200)
        # call the method to test
        test_service = User("testkey")
        response = test_service.register_user({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_register_user_error_on_non_200(self):
        # Mock the API response
        responses.post("http://localhost:8080/user", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = User("testkey")
            test_service.register_user({})
        responses.reset()


if __name__ == "__main__":
    unittest.main()
