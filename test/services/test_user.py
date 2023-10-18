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
            "http://localhost:8000/user/?Q|j%TCe=C|`\\0aB(!I+GPsa!3X!xz.@)#0}prvCiwX%\\dViS{k!L L>79,)hRJ7'*7.n1iRLKvz<}Xzg_IH[edO.2B;|/6Ht*EjA;#*rY::VI7zBq`:<E+a9~5A@%K#I.?EvB{0_NqVOT[d S4\\58Z>x{^yy'-=7!-b",
            json={},
            status=200,
        )
        # call the method to test
        test_service = User("testkey")
        response = test_service.get_user_by_email(
            "?Q|j%TCe=C|`\\0aB(!I+GPsa!3X!xz.@)#0}prvCiwX%\\dViS{k!L L>79,)hRJ7'*7.n1iRLKvz<}Xzg_IH[edO.2B;|/6Ht*EjA;#*rY::VI7zBq`:<E+a9~5A@%K#I.?EvB{0_NqVOT[d S4\\58Z>x{^yy'-=7!-b"
        )
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_user_by_email_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://localhost:8000/user/I;N@;j0I1vl^uf19@`>#r_'OjpnB7tv@)xh$'!2yq)]93\"zindK_p>FL.BO})3QW!OtVlCl@(5xet;!,Igo1v<0/5*JcoH)4T^@A[C=\\`|DG'I.n?F3#[ ?wsz@_? L,..v*",
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
            "http://localhost:8000/user/nNv`b]Zo@@!otbba8>zl?YL5/7FN5}d=My<pE s/%3]m4ZSQ\\FB+\\ToFRC^.`w^jafZm,q]h{4 m_%oQb?z+n[}|B|JLqH<a9v,2WrOlyL6qZ",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = User("testkey")
            test_service.get_user_by_email(
                "nNv`b]Zo@@!otbba8>zl?YL5/7FN5}d=My<pE s/%3]m4ZSQ\\FB+\\ToFRC^.`w^jafZm,q]h{4 m_%oQb?z+n[}|B|JLqH<a9v,2WrOlyL6qZ"
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
