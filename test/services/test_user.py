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
            'http://localhost:8000/user/+fDB^w[ucCPdz!a cP&CPIcL\\DdQ(b/x;Ai:f[A^+MrcZ^[+3lM3,Z@lM0hXy>[@Kcno&Hr}:!F"d2*$b;dg!q\\7>KeNJ{EGDx}\\<fqc:j0.zux2ynB:T1[WB"uT=FjXy*T|6Xz94DmBvJa+Vgx\'+xzq?t{bdzOy%',
            json={},
            status=200,
        )
        # call the method to test
        test_service = User("testkey")
        response = test_service.get_user_by_email(
            '+fDB^w[ucCPdz!a cP&CPIcL\\DdQ(b/x;Ai:f[A^+MrcZ^[+3lM3,Z@lM0hXy>[@Kcno&Hr}:!F"d2*$b;dg!q\\7>KeNJ{EGDx}\\<fqc:j0.zux2ynB:T1[WB"uT=FjXy*T|6Xz94DmBvJa+Vgx\'+xzq?t{bdzOy%'
        )
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_user_by_email_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://localhost:8000/user/Czba$++2R$do19~h;-lKbbDPM$blo_ds3vg_]8r^Gb z)Cd'XS5SV=!GsiSt~[s??CUk#PqNO}3R5^V?@^X\\<Rgc@>g.*5xY{j gT s.Mvz2v_lS\\46yBUn6/f6I8jyS\\flWNKm@wom?Kcl\"hZ~=.UU=uhK9apc8P%`yP(`]c []PJmB'D`p(cGvcxDeJWEL>@(J\"F`'davi\"jka1|=",
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
            'http://localhost:8000/user/YiHR5Z%}~u_^Z4gg"\\H1h{bV@S-d`iyu0dNvU%(V6%F-}"iD7g^sd^!f"x^mFc3fo`.7bY1:Q".it[HG"n@yi< XF\\Cm/twYk|,8Ws3Rk.#/k&DSv8"l0eS`g)[pGN:[S^)$UyC-0|',
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = User("testkey")
            test_service.get_user_by_email(
                'YiHR5Z%}~u_^Z4gg"\\H1h{bV@S-d`iyu0dNvU%(V6%F-}"iD7g^sd^!f"x^mFc3fo`.7bY1:Q".it[HG"n@yi< XF\\Cm/twYk|,8Ws3Rk.#/k&DSv8"l0eS`g)[pGN:[S^)$UyC-0|'
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
