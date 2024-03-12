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
            'http://localhost:8080/user/%tD_W5RfO~{Ehg?>R:cRC3}dW$F!\\"z+{I@iH"i%B>B^w.OY&Azw@S9(X=dawe` P,p<a7NK`U Pv3B0k3n[Sa&{FDKPOCe(\'s(x6bhgQ#^ygN6g40P?~"sZSGCA7oGI>t"~#q5|O"|~.KgRW-J4t7KM[XGE/<7{e\\yQXGP:tq?gN',
            json={},
            status=200,
        )
        # call the method to test
        test_service = User("testkey")
        response = test_service.get_user_by_email(
            '%tD_W5RfO~{Ehg?>R:cRC3}dW$F!\\"z+{I@iH"i%B>B^w.OY&Azw@S9(X=dawe` P,p<a7NK`U Pv3B0k3n[Sa&{FDKPOCe(\'s(x6bhgQ#^ygN6g40P?~"sZSGCA7oGI>t"~#q5|O"|~.KgRW-J4t7KM[XGE/<7{e\\yQXGP:tq?gN'
        )
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_user_by_email_required_fields_missing(self):
        # Mock the API response
        responses.get(
            'http://localhost:8080/user/VP@?_5vt;7;qmB2C2v7EX%3aCxn6rqd.%cR[Z4A&f39D%c?ey>a&tl99lgiqo@x%:OfZO RK0@ApoWU!E#B0+"VhdL590,qVa8=%-OabjrIn$<eBam/Mbl]C8C.[T;^%G2\\D4~RqxY#&%QPP^#oataywCv1YpjE}L%B?wMhl>rVce\\A2NK:MBL9.;w0d !@CEY+HF',
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
            "http://localhost:8080/user/N]OuG4fjS1Ry8m%b>twb5'Tb$aL@ubIWa3o3e;GRycTlzJSY%Z`Gpfnfw.)S6}K\\FJ,fN7WZ3JZ3s&dtK3{zWo5*",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = User("testkey")
            test_service.get_user_by_email(
                "N]OuG4fjS1Ry8m%b>twb5'Tb$aL@ubIWa3o3e;GRycTlzJSY%Z`Gpfnfw.)S6}K\\FJ,fN7WZ3JZ3s&dtK3{zWo5*"
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
