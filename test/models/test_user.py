import unittest
from src.llamastore.models.User import User


class TestUserModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_user(self):
        # Create User class instance
        test_model = User(
            id=6,
            email='E1_*-l`3$]\\QKJQBXIOi&7VBHfM~Nld3Nm2;=DDNO6d8M"_B~90]hPcJ~M|shwKs@-yP5Skx\\f~3UZs$Vz"L5u}>5+"}US}8R4$i!}>nDAyCRh"jWoC\\@NarcPx4m~3ciG2=3XC)d5wc/>Tg.wn"f?Qcq9+s&iRS_*eDJ!(jRM#gs|8^A1($%kf9iA:\'',
        )
        self.assertEqual(test_model.id, 6)
        self.assertEqual(
            test_model.email,
            'E1_*-l`3$]\\QKJQBXIOi&7VBHfM~Nld3Nm2;=DDNO6d8M"_B~90]hPcJ~M|shwKs@-yP5Skx\\f~3UZs$Vz"L5u}>5+"}US}8R4$i!}>nDAyCRh"jWoC\\@NarcPx4m~3ciG2=3XC)d5wc/>Tg.wn"f?Qcq9+s&iRS_*eDJ!(jRM#gs|8^A1($%kf9iA:\'',
        )

    def test_user_required_fields_missing(self):
        # Assert User class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = User()


if __name__ == "__main__":
    unittest.main()
