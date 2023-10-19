import unittest
from src.llamastore.models.UserRegistration import UserRegistration


class TestUserRegistrationModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_user_registration(self):
        # Create UserRegistration class instance
        test_model = UserRegistration(
            password="voluptates",
            email="^bQIzaB]jK+G4uHX9GuE|8)r?,u>l{H7y!qttp [1'CN+1#J/2>_:>ptJf-@I{Jqxl>;OS\"}-(H\\EA6d}G@gDViLRH:Reuvspe=FUC.he+OBM6Q#&oP-~1DXmW.5}Z *#,5cNp54v'q",
        )
        self.assertEqual(test_model.password, "voluptates")
        self.assertEqual(
            test_model.email,
            "^bQIzaB]jK+G4uHX9GuE|8)r?,u>l{H7y!qttp [1'CN+1#J/2>_:>ptJf-@I{Jqxl>;OS\"}-(H\\EA6d}G@gDViLRH:Reuvspe=FUC.he+OBM6Q#&oP-~1DXmW.5}Z *#,5cNp54v'q",
        )

    def test_user_registration_required_fields_missing(self):
        # Assert UserRegistration class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UserRegistration()


if __name__ == "__main__":
    unittest.main()
