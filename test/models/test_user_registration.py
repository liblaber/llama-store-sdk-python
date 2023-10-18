import unittest
from src.llamastore.models.UserRegistration import UserRegistration


class TestUserRegistrationModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_user_registration(self):
        # Create UserRegistration class instance
        test_model = UserRegistration(
            password="vero",
            email="/_Ne'1o#/2z,hyfD>(]VdCl/vI2k`k.?246}@A)E]H:(aao`]2{JXW79~@?UpM 3%v~:4.t<tr]srj|YfZ(=~:8wa6+NqjimkhPhzm4(lR_()nphfY=],|cv\\)m2$t&-AYl$Ta%4Q/UU<`ffkg~iCrQ#rEjL{y2",
        )
        self.assertEqual(test_model.password, "vero")
        self.assertEqual(
            test_model.email,
            "/_Ne'1o#/2z,hyfD>(]VdCl/vI2k`k.?246}@A)E]H:(aao`]2{JXW79~@?UpM 3%v~:4.t<tr]srj|YfZ(=~:8wa6+NqjimkhPhzm4(lR_()nphfY=],|cv\\)m2$t&-AYl$Ta%4Q/UU<`ffkg~iCrQ#rEjL{y2",
        )

    def test_user_registration_required_fields_missing(self):
        # Assert UserRegistration class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UserRegistration()


if __name__ == "__main__":
    unittest.main()
