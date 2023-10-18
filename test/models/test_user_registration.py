import unittest
from src.llamastore.models.UserRegistration import UserRegistration


class TestUserRegistrationModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_user_registration(self):
        # Create UserRegistration class instance
        test_model = UserRegistration(
            password="corporis",
            email="TJ-{SS.Dc'JtiTEy.q_)ju`9;B/QR1lYrv[x[%Eo8Tl@;!&-0}W'bo#RG6qIM\\'~zCxwZZI]c5K7N7;@n)vncnbs^GQ.MA%6N9Eur7{YF6hVpeEV;M~0Iw0JPSkX",
        )
        self.assertEqual(test_model.password, "corporis")
        self.assertEqual(
            test_model.email,
            "TJ-{SS.Dc'JtiTEy.q_)ju`9;B/QR1lYrv[x[%Eo8Tl@;!&-0}W'bo#RG6qIM\\'~zCxwZZI]c5K7N7;@n)vncnbs^GQ.MA%6N9Eur7{YF6hVpeEV;M~0Iw0JPSkX",
        )

    def test_user_registration_required_fields_missing(self):
        # Assert UserRegistration class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UserRegistration()


if __name__ == "__main__":
    unittest.main()
