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
            "http://localhost:8080/user/\"&N~i>zl=[FU$qpKbwx>q& SAn'eP0aXzs4@<,OAV8Mh>QQk_7F6(%>&[[K%r\\<sc>.(]]%xSti",
            json={},
            status=200,
        )
        # call the method to test
        test_service = User("testkey")
        response = test_service.get_user_by_email(
            "\"&N~i>zl=[FU$qpKbwx>q& SAn'eP0aXzs4@<,OAV8Mh>QQk_7F6(%>&[[K%r\\<sc>.(]]%xSti"
        )
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_user_by_email_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://localhost:8080/user/U0klHb;l(T1\\%eCf(,&6D~!ZeM,WHdQbkRj:gV@F|86|qNA!Tu:zazt'ekR$q| ZO +P&%qNp;+]an(ea j&<f[8}!y~(k27k#|7',/]N_OK=s~A.g8=g SK6n.kMubK.f2r!sWZ7]^*mJeJ2d >,gG$oPl{B#7d^>hd%/vkKWFyafj21",
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
            "http://localhost:8080/user/8#n!+$_}')U(D kR)\\2!N_Nx@5h%$}f/POdYLpRx_X(`M\\OFf|?YA'nWo`v~etJFfqIR?K8:ylc@boit(%'4+@.L9-zcwi8E>?sb:BtH`&\\~/5jAWZY.g&crPY:diHr<Bz`4IGw4:*QI: LLyzM~{4? -YjfhM?&$YMh_uQP~e20&,+m}U`K8/TqumCubiy};/ZUD(mQD*O1",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = User("testkey")
            test_service.get_user_by_email(
                "8#n!+$_}')U(D kR)\\2!N_Nx@5h%$}f/POdYLpRx_X(`M\\OFf|?YA'nWo`v~etJFfqIR?K8:ylc@boit(%'4+@.L9-zcwi8E>?sb:BtH`&\\~/5jAWZY.g&crPY:diHr<Bz`4IGw4:*QI: LLyzM~{4? -YjfhM?&$YMh_uQP~e20&,+m}U`K8/TqumCubiy};/ZUD(mQD*O1"
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
