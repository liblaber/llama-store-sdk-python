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
            'http://localhost:8000/user/ZSE4%:SX?336qK@1B4/-ffLtkh+7m"4j5K1n{f<H)o|~I~-H;9ZX3YK0B\\BjFK6%+ZOjKd$^2CTb];%`Mc"CI${$o4M@E#Q\\6t3s$jAj4:WR9TTNa\'1PGfY3~j!b9:x.KZsW2)v',
            json={},
            status=200,
        )
        # call the method to test
        test_service = User("testkey")
        response = test_service.get_user_by_email(
            'ZSE4%:SX?336qK@1B4/-ffLtkh+7m"4j5K1n{f<H)o|~I~-H;9ZX3YK0B\\BjFK6%+ZOjKd$^2CTb];%`Mc"CI${$o4M@E#Q\\6t3s$jAj4:WR9TTNa\'1PGfY3~j!b9:x.KZsW2)v'
        )
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_user_by_email_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://localhost:8000/user/O<{Ig?DVYV7lz_.eus,PVx<oL8!A{cL;LUAeivT+uI2<T2N/L<Vveud`jMf`U,%UFc5&?F9UZuhe*^T< @sU[G,'!\">]0Y6z+N*d]M;x=hgbCxi^S)H1S.]viU,-rdSyB+X\\qI?5+]fLoO/1|;\\%dny\\-zFid*O3",
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
            'http://localhost:8000/user/~jB"q6vYt!DhxoaS1ZLnHeYK\\XIo,$[FHc"1[[C1E@$5{?eohK7&?>=;0q^bJ5D8LQ!_Q6n/4FRcY 6MrPI\\0!a0zv<`O~;)_AE#HyzOKrmnvv-@d5nI`O.4&Tx* ,e./user/P2D:~P3(c=]bG{V "@/d;%{fXfqy)Ct`Cyd>%tPq+)pxYz}jc46_>+hkZp ++%2,+f%h8s#`Ke[Q_|y[',
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = User("testkey")
            test_service.get_user_by_email(
                '~jB"q6vYt!DhxoaS1ZLnHeYK\\XIo,$[FHc"1[[C1E@$5{?eohK7&?>=;0q^bJ5D8LQ!_Q6n/4FRcY 6MrPI\\0!a0zv<`O~;)_AE#HyzOKrmnvv-@d5nI`O.4&Tx* ,e.$`P2D:~P3(c=]bG{V "@/d;%{fXfqy)Ct`Cyd>%tPq+)pxYz}jc46_>+hkZp ++%2,+f%h8s#`Ke[Q_|y['
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
