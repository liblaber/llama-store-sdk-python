import unittest
from src.llamastore.models.UserRegistration import UserRegistration


class TestUserRegistrationModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_user_registration(self):
        # Create UserRegistration class instance
        test_model = UserRegistration(
            password="sapiente",
            email="!j3/J$Nfe-Xws4D/`>=.AvKtOa=@!Nx$@co,~BY.VU-<%@pD>*4rVQj{xYkt>-`VHt+HR\\.p6C68?$;|PAa/3{xo,qgx.p%h^NZ}^]+kh8a.)uwi}1Z{.5&K`f$0&j|iRcUA[u~*//`7on$)\\ ?[f(}Yp#CzPXnRQ3aPFlRQ4iSW`6u~WX.oJ\\;`!xgsr#v9",
        )
        self.assertEqual(test_model.password, "sapiente")
        self.assertEqual(
            test_model.email,
            "!j3/J$Nfe-Xws4D/`>=.AvKtOa=@!Nx$@co,~BY.VU-<%@pD>*4rVQj{xYkt>-`VHt+HR\\.p6C68?$;|PAa/3{xo,qgx.p%h^NZ}^]+kh8a.)uwi}1Z{.5&K`f$0&j|iRcUA[u~*//`7on$)\\ ?[f(}Yp#CzPXnRQ3aPFlRQ4iSW`6u~WX.oJ\\;`!xgsr#v9",
        )

    def test_user_registration_required_fields_missing(self):
        # Assert UserRegistration class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UserRegistration()


if __name__ == "__main__":
    unittest.main()
