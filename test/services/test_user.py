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
            "http://localhost:8000/user/ZMKw1;`5fcGEK57sWcMK>O7^sY+_l@d^Q:UK_POp\"0= ax(UU5r~Z9}-3CdC_NI5dhapMQ_L YEUm[`YPP2@<YRcw9K3yE`~-3rr48J`|Wh!lM*`o}aU?I(F.:,`~^$f.|VvPxG)Cij}E$Z8_N}P#mWorM'usQKd0'oABl>OJI=V@2UY}=mE#LK3OOS4X.0\\XOo3-?.T :4f/{",
            json={},
            status=200,
        )
        # call the method to test
        test_service = User("testkey")
        response = test_service.get_user_by_email(
            "ZMKw1;`5fcGEK57sWcMK>O7^sY+_l@d^Q:UK_POp\"0= ax(UU5r~Z9}-3CdC_NI5dhapMQ_L YEUm[`YPP2@<YRcw9K3yE`~-3rr48J`|Wh!lM*`o}aU?I(F.:,`~^$f.|VvPxG)Cij}E$Z8_N}P#mWorM'usQKd0'oABl>OJI=V@2UY}=mE#LK3OOS4X.0\\XOo3-?.T :4f/{"
        )
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_user_by_email_required_fields_missing(self):
        # Mock the API response
        responses.get(
            'http://localhost:8000/user/}~FML~\\U4")s!{OU,0Z{-k"gFE\\rt|Hw$+r9r2J{@HS&|i<C7gjgq^eptLgEm9&GX+57Ks&*|*)"3(pv.Qt+|>t$6mE.<N5u_6\'o1r]Dj#WJ$zL^l`T]?;`',
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
            'http://localhost:8000/user//["3lCdsdbc7&_%{8K-"(I@3\\Cn-{\'gmIp[*\\@q[iPDk9IhrUUxA-j=kG\\La.wbx8eh,^z8ZA3e6dQT+f|<MO1+!yt;5t#~9\\2/k@?u9Z9M.r&`@u{q.|{9',
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = User("testkey")
            test_service.get_user_by_email(
                '/["3lCdsdbc7&_%{8K-"(I@3\\Cn-{\'gmIp[*\\@q[iPDk9IhrUUxA-j=kG\\La.wbx8eh,^z8ZA3e6dQT+f|<MO1+!yt;5t#~9\\2/k@?u9Z9M.r&`@u{q.|{9'
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
