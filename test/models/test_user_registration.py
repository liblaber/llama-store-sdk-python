import unittest
from src.llamastore.models.UserRegistration import UserRegistration


class TestUserRegistrationModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_user_registration(self):
        # Create UserRegistration class instance
        test_model = UserRegistration(
            password="voluptatibus",
            email='`t=y}6sP2nPT&.)W#JzcCj&1cBL9Gj<[U,3SPj{:%|d6emlkOb,hd_@tsl-4.>z|OX`l?uwOFgNLxQ@iU+V/<dey.xh1@&]bJRcNPBS} Qi(-g3+8p|,f+2#@]+tN,a-0wQBny-I+o5@W!"6RUqFc-z5PUa$FMF\\gSXEdR(F5MXf0+',
        )
        self.assertEqual(test_model.password, "voluptatibus")
        self.assertEqual(
            test_model.email,
            '`t=y}6sP2nPT&.)W#JzcCj&1cBL9Gj<[U,3SPj{:%|d6emlkOb,hd_@tsl-4.>z|OX`l?uwOFgNLxQ@iU+V/<dey.xh1@&]bJRcNPBS} Qi(-g3+8p|,f+2#@]+tN,a-0wQBny-I+o5@W!"6RUqFc-z5PUa$FMF\\gSXEdR(F5MXf0+',
        )

    def test_user_registration_required_fields_missing(self):
        # Assert UserRegistration class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UserRegistration()


if __name__ == "__main__":
    unittest.main()
