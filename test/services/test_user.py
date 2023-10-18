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
            "http://localhost:8000/user/k+^bd#06-!+pCb T8NV!!['60F.A7;Dj^[e=HAaKr6B5<z:(<c_u_b@{Lvggs9&HCxS|&Ely;pksQg.w2*pgE\\FQruoG?vLMtu",
            json={},
            status=200,
        )
        # call the method to test
        test_service = User("testkey")
        response = test_service.get_user_by_email(
            "k+^bd#06-!+pCb T8NV!!['60F.A7;Dj^[e=HAaKr6B5<z:(<c_u_b@{Lvggs9&HCxS|&Ely;pksQg.w2*pgE\\FQruoG?vLMtu"
        )
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_user_by_email_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://localhost:8000/user/&hhFo6]m\\yeI;=@Lbmub.ye6-fxF1-b9n&5UReQ!8sY0l5p$c M0xN|+= @\\)!`=(\\9~)Vh1_z^Kt*mh ];i]jL9j|nb{m~.,AhKvNw'=L'R7`V51}-`6!(u-I!tJ0p1+CiJlJH7oXAiM}N@m.9I%?|a;pg0*.[",
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
            "http://localhost:8000/user/!*Zj/pGt2,EJe`=W~Hdkb,I3yaqdDQ_lgHGI{+=eaH`(GXVZ-8/x3@2  (+~JE{xi3qZ`?BTN ZiXt@vT}wCxoRm.7",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = User("testkey")
            test_service.get_user_by_email(
                "!*Zj/pGt2,EJe`=W~Hdkb,I3yaqdDQ_lgHGI{+=eaH`(GXVZ-8/x3@2  (+~JE{xi3qZ`?BTN ZiXt@vT}wCxoRm.7"
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
