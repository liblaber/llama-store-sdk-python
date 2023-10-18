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
            "http://localhost:8000/user/CFtBCq?uJ{<]HC#_;U5HJ$U'D<xYm<aOs}f38tHUK^\"/*:+}|*5e?P*'-+ZF0<dDp9@4O0pR*/@vnvY{@9 wDm%hzG(`*2eTu:#p}X>(B!a%%%pu'%.M_Zd~^lSa- g#)[=tW>o`H0@T_t:hF\\E$[3-|U~h)25E:WqY)UcjRVV|R]/.&xq2rnXy?9r_n.{Po{Dww<GkJUR2r:O`_A7`l>C&kH@",
            json={},
            status=200,
        )
        # call the method to test
        test_service = User("testkey")
        response = test_service.get_user_by_email(
            "CFtBCq?uJ{<]HC#_;U5HJ$U'D<xYm<aOs}f38tHUK^\"/*:+}|*5e?P*'-+ZF0<dDp9@4O0pR*/@vnvY{@9 wDm%hzG(`*2eTu:#p}X>(B!a%%%pu'%.M_Zd~^lSa- g#)[=tW>o`H0@T_t:hF\\E$[3-|U~h)25E:WqY)UcjRVV|R]/.&xq2rnXy?9r_n.{Po{Dww<GkJUR2r:O`_A7`l>C&kH@"
        )
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_user_by_email_required_fields_missing(self):
        # Mock the API response
        responses.get(
            'http://localhost:8000/user/$2"8k8bw<Jb}R.Wv)l0R2XVMOs"\\5~c!<J{\\[w{1K3Ni%x.X!e6-z@]K$(@Zh(L_#BWB9\\v7B5o{PcFn72@-Bv&x5E`y,5SOrIbiGhb@OZ8jO0!\'HsrXg}CsPXKwuz.KO?tJ!D4/Pb?wf`QY:w#0W:T~',
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
            "http://localhost:8000/user/7nq#i0J)'KN>x, d@jmq3]8n&0q!@Igk[+6]A7R8}+%>icy^f'x(j{Xw$jfj'>fgR./q!ANYY|R?_95+)e0cE,dgA",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = User("testkey")
            test_service.get_user_by_email(
                "7nq#i0J)'KN>x, d@jmq3]8n&0q!@Igk[+6]A7R8}+%>icy^f'x(j{Xw$jfj'>fgR./q!ANYY|R?_95+)e0cE,dgA"
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
