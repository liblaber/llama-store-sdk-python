import unittest
from src.llamastore.models.User import User


class TestUserModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_user(self):
        # Create User class instance
        test_model = User(
            id=1,
            email='`ApBj`k}(sMX&L]urX$rteIQ$=Y[.JvQ5Nzg6VdqijEA_Hle/V&z<iGFg+/B3;g,!YtJ6?zk6;u\\&w`xY@.~M"b%*p7&*me(\'BK_"bkj;1{uvF+M\\h;-}`(}":qLPjyqR?M~q2{o+^L0>NBM\'>`[I{Ict0%4$>Ekb}I)P{g%-nPw.E48ZO*',
        )
        self.assertEqual(test_model.id, 1)
        self.assertEqual(
            test_model.email,
            '`ApBj`k}(sMX&L]urX$rteIQ$=Y[.JvQ5Nzg6VdqijEA_Hle/V&z<iGFg+/B3;g,!YtJ6?zk6;u\\&w`xY@.~M"b%*p7&*me(\'BK_"bkj;1{uvF+M\\h;-}`(}":qLPjyqR?M~q2{o+^L0>NBM\'>`[I{Ict0%4$>Ekb}I)P{g%-nPw.E48ZO*',
        )

    def test_user_required_fields_missing(self):
        # Assert User class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = User()


if __name__ == "__main__":
    unittest.main()
