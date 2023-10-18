import unittest
from src.llamastore.models.User import User


class TestUserModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_user(self):
        # Create User class instance
        test_model = User(
            id=6,
            email='!F\\UM;"D<i)D,M]3C7|iAf*)49f}_Cb\\-# X68@m{sdM8~#H):IH!iSJS9J-}ZYRQ]eAj#%-X`"+KSuc_{!G,`~XDIy%56J[<r4v3wc~_A-SnRukeEmXI`s+L/$0tXOd.)Qv$F*77yUb)Y8$<DfCL\\^\\jgxpPR(FDir;!,y(W(x\\',
        )
        self.assertEqual(test_model.id, 6)
        self.assertEqual(
            test_model.email,
            '!F\\UM;"D<i)D,M]3C7|iAf*)49f}_Cb\\-# X68@m{sdM8~#H):IH!iSJS9J-}ZYRQ]eAj#%-X`"+KSuc_{!G,`~XDIy%56J[<r4v3wc~_A-SnRukeEmXI`s+L/$0tXOd.)Qv$F*77yUb)Y8$<DfCL\\^\\jgxpPR(FDir;!,y(W(x\\',
        )

    def test_user_required_fields_missing(self):
        # Assert User class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = User()


if __name__ == "__main__":
    unittest.main()
