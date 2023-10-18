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
            "http://localhost:8000/user/x/PnF'W: @2hP]CGv\"f3x/<TC:oJ#v[N=K.wt{",
            json={},
            status=200,
        )
        # call the method to test
        test_service = User("testkey")
        response = test_service.get_user_by_email(
            "x/PnF'W: @2hP]CGv\"f3x/<TC:oJ#v[N=K.wt{"
        )
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_user_by_email_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://localhost:8000/user/3EOy6f{6i{o_UFk^xO{<:&z8@X~sBH>2,M)Jpi`#=Ozdk!`-KXqeC(@3xzZITA!1WwdXu>=:F9P5o %a06kG?oI#'z3_HS;@zXlznFIXv#d2O.:rJKn]edhE zAZ\\EDwNb5.]:7f9hS>z$\"G2HS#VRm1~VJ;4{r:]p'MOpre([Q&~",
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
            'http://localhost:8000/user/?Ag<1kW9V[$RmPG;JV)CqMT8ftb4FV\'\\R.!/dV[^p/S4C`T-nP},~`9c;r/P[\'$JD\\:/M-{&>E>OEM,F`@T [Kz#<pw"A>$ v^=-lT:")"Q?3B2k^.MVMp)]i$*%HTYLV%h|n]6[?`!pl7L',
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = User("testkey")
            test_service.get_user_by_email(
                '?Ag<1kW9V[$RmPG;JV)CqMT8ftb4FV\'\\R.!/dV[^p/S4C`T-nP},~`9c;r/P[\'$JD\\:/M-{&>E>OEM,F`@T [Kz#<pw"A>$ v^=-lT:")"Q?3B2k^.MVMp)]i$*%HTYLV%h|n]6[?`!pl7L'
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
