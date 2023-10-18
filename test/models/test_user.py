import unittest
from src.llamastore.models.User import User


class TestUserModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_user(self):
        # Create User class instance
        test_model = User(
            id=4,
            email="rLNCEnv`Jr7w'9!A-%NG[va#@~F02+.\\O+OQh&mCcI@ 74!ym>~xoqU0z&oUC8kI.l&s.\\.7H%LJ-\"(0pqQ4bZ)<T'HrtT .+f:H9^37EGHH!#5*!WJexm(=: +&5VB75e29C(] C*ZivBd5<3Oeh0:",
        )
        self.assertEqual(test_model.id, 4)
        self.assertEqual(
            test_model.email,
            "rLNCEnv`Jr7w'9!A-%NG[va#@~F02+.\\O+OQh&mCcI@ 74!ym>~xoqU0z&oUC8kI.l&s.\\.7H%LJ-\"(0pqQ4bZ)<T'HrtT .+f:H9^37EGHH!#5*!WJexm(=: +&5VB75e29C(] C*ZivBd5<3Oeh0:",
        )

    def test_user_required_fields_missing(self):
        # Assert User class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = User()


if __name__ == "__main__":
    unittest.main()
