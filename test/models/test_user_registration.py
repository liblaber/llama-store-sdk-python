import unittest
from src.llamastore.models.UserRegistration import UserRegistration


class TestUserRegistrationModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_user_registration(self):
        # Create UserRegistration class instance
        test_model = UserRegistration(
            password="doloremque",
            email='4nS?rEt_{K^sG[\\6m-`Q<[H]=^|5iRZS8.|r@wz:-%67axC)EMqD)sV\\h|d!O_8=/&;=vi<|B8NWE:"bfAMe\'wX;[J&XAAEb~&;5yRKA~=*y#[S|Mt~MNk3wi"/WFXvyd.8lfBxpT3riTa!3NKF^SE`BpL{&{k=k0UckI}',
        )
        self.assertEqual(test_model.password, "doloremque")
        self.assertEqual(
            test_model.email,
            '4nS?rEt_{K^sG[\\6m-`Q<[H]=^|5iRZS8.|r@wz:-%67axC)EMqD)sV\\h|d!O_8=/&;=vi<|B8NWE:"bfAMe\'wX;[J&XAAEb~&;5yRKA~=*y#[S|Mt~MNk3wi"/WFXvyd.8lfBxpT3riTa!3NKF^SE`BpL{&{k=k0UckI}',
        )

    def test_user_registration_required_fields_missing(self):
        # Assert UserRegistration class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UserRegistration()


if __name__ == "__main__":
    unittest.main()
