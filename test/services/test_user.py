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
            "http://localhost:8000/user//{\\`^M3\\ngEF;-TUrBtLFk%oJF~<@qE`jO>@sVInN^aR1@%}n]ImbCQ7DuY9ox*>a(H^rGA<n\"y6Ots@11tq@F? Sa8gma@L0N'i|\\Yth8.T_;be2MugN O!GHNDIEUv3fN.)eN3ECkb)|F`h>i{9y",
            json={},
            status=200,
        )
        # call the method to test
        test_service = User("testkey")
        response = test_service.get_user_by_email(
            "/{\\`^M3\\ngEF;-TUrBtLFk%oJF~<@qE`jO>@sVInN^aR1@%}n]ImbCQ7DuY9ox*>a(H^rGA<n\"y6Ots@11tq@F? Sa8gma@L0N'i|\\Yth8.T_;be2MugN O!GHNDIEUv3fN.)eN3ECkb)|F`h>i{9y"
        )
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_user_by_email_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://localhost:8000/user/=.ANU]qveMK@E3.44w~A'El\"}qAVA*d(\\zWSJOV0#\\J.^h,fOuJrBu56ASfX0u6L0&WwK`}t@PbnI._sDstxlG9`bv",
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
            "http://localhost:8000/user/|i 01+lZ> 'aD!*k=V\"5,~9SI`48h+R#4\\|)v4!>/l1g]-A@l^4P7bLbi^G&&0B\\`,YSI/@0;FL9%_@l`/]wyu1J3ga 6c!yut*S.1O0rE!\\tJBI^3~ n-kWF6&oyq\\$UU)x_JEfl+EhVR~.FN;B.pM,$MW58EkwIVbtqg^OW=qJ9^t;h17.D4",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = User("testkey")
            test_service.get_user_by_email(
                "|i 01+lZ> 'aD!*k=V\"5,~9SI`48h+R#4\\|)v4!>/l1g]-A@l^4P7bLbi^G&&0B\\`,YSI/@0;FL9%_@l`/]wyu1J3ga 6c!yut*S.1O0rE!\\tJBI^3~ n-kWF6&oyq\\$UU)x_JEfl+EhVR~.FN;B.pM,$MW58EkwIVbtqg^OW=qJ9^t;h17.D4"
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
