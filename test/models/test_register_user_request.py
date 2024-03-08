import unittest
from src.llamastore.models.RegisterUserRequest import RegisterUserRequest


class TestRegisterUserRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_register_user_request(self):
        # Create RegisterUserRequest class instance
        test_model = RegisterUserRequest(
            password="error",
            email='78}ExHh?>)J\\t1Ioh-T|$OZE  @fx/Z.Mtu{?PhSe<O#q3r&6E%=(g4;Bw](*luah+7F=4Xi.~jN`h`w0^wd#xm";gqsCMIp*W.YrGLDrRADL',
        )
        self.assertEqual(test_model.password, "error")
        self.assertEqual(
            test_model.email,
            '78}ExHh?>)J\\t1Ioh-T|$OZE  @fx/Z.Mtu{?PhSe<O#q3r&6E%=(g4;Bw](*luah+7F=4Xi.~jN`h`w0^wd#xm";gqsCMIp*W.YrGLDrRADL',
        )

    def test_register_user_request_required_fields_missing(self):
        # Assert RegisterUserRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = RegisterUserRequest()


if __name__ == "__main__":
    unittest.main()
