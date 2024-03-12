import unittest
from src.llamastore.models.RegisterUserRequest import RegisterUserRequest


class TestRegisterUserRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_register_user_request(self):
        # Create RegisterUserRequest class instance
        test_model = RegisterUserRequest(
            password="animi",
            email="aA(kUK6O~aem>@1Fvg\\k'x`2_kOdseAE-xK[mrK:F@!t%UGsW){)`7;Na+7lpV,j'K\"$1&hGb2.Dqiin,6<[S.\\KzG8.F4Lp\"3ZBF:4Mx$f7m$=MIbW$0T}=[!(U5+:qae?.N",
        )
        self.assertEqual(test_model.password, "animi")
        self.assertEqual(
            test_model.email,
            "aA(kUK6O~aem>@1Fvg\\k'x`2_kOdseAE-xK[mrK:F@!t%UGsW){)`7;Na+7lpV,j'K\"$1&hGb2.Dqiin,6<[S.\\KzG8.F4Lp\"3ZBF:4Mx$f7m$=MIbW$0T}=[!(U5+:qae?.N",
        )

    def test_register_user_request_required_fields_missing(self):
        # Assert RegisterUserRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = RegisterUserRequest()


if __name__ == "__main__":
    unittest.main()
