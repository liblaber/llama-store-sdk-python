import unittest
from src.llamastore.models.User import User


class TestUserModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_user(self):
        # Create User class instance
        test_model = User(
            id=9,
            email="Si %hk5//:*rF;4ZRqejyY*XK@~DOAzM<QO30 WgHo~q#3.xZg*6gMgF$t):n.y\"ZKz_Pdz32kkBxo><+>0<bBbt[dw#@jkZM.<GErkL1:ZE`Xb]!m9$6]< v%Cz%Wrn|kp@*bV2X;:x>xn''CJ*>uJl7rW^_BB>K'G`4Hk#?Y_yNj4ebve&4.pzId[O62=/?9wI|9fsLq",
        )
        self.assertEqual(test_model.id, 9)
        self.assertEqual(
            test_model.email,
            "Si %hk5//:*rF;4ZRqejyY*XK@~DOAzM<QO30 WgHo~q#3.xZg*6gMgF$t):n.y\"ZKz_Pdz32kkBxo><+>0<bBbt[dw#@jkZM.<GErkL1:ZE`Xb]!m9$6]< v%Cz%Wrn|kp@*bV2X;:x>xn''CJ*>uJl7rW^_BB>K'G`4Hk#?Y_yNj4ebve&4.pzId[O62=/?9wI|9fsLq",
        )

    def test_user_required_fields_missing(self):
        # Assert User class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = User()


if __name__ == "__main__":
    unittest.main()
