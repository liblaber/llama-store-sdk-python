import unittest
from src.llamastore.models.User import User


class TestUserModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_user(self):
        # Create User class instance
        test_model = User(
            id=9,
            email="EB2@5:mAuV^xcS'8PD*NZ7:V<;9As(D5 uEp_Tu~KOEt*yQMFM2R%;<)Tp/zlfKW:d>?SNSx9,.Fw-5U9>l~00_(wRK;olD-_2j!w_Dy`h.%%%l+B6II-j6qM(bdVaNb/=}g3^\\RL<e-n5I u;wM W5<;,o-e#$,68jt]0v;,p4Fo",
        )
        self.assertEqual(test_model.id, 9)
        self.assertEqual(
            test_model.email,
            "EB2@5:mAuV^xcS'8PD*NZ7:V<;9As(D5 uEp_Tu~KOEt*yQMFM2R%;<)Tp/zlfKW:d>?SNSx9,.Fw-5U9>l~00_(wRK;olD-_2j!w_Dy`h.%%%l+B6II-j6qM(bdVaNb/=}g3^\\RL<e-n5I u;wM W5<;,o-e#$,68jt]0v;,p4Fo",
        )

    def test_user_required_fields_missing(self):
        # Assert User class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = User()


if __name__ == "__main__":
    unittest.main()
