import unittest
from src.llamastore.models.User import User


class TestUserModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_user(self):
        # Create User class instance
        test_model = User(
            id=1,
            email="lmpNzAn@iAW43-Sj]8\"x*7ag#D'Fl&3i%tz'xNd(GM&k48UCfb3`@xFHUMTxlxl@#1hx);!-/Qkq(:mjXIAX'R-FF[CmyfS*c9}~3PR#=2]g=9DBENDWiSXX9h&r=O+oK};;;C6.Dtr{p+gYh+1*xL|-vl)x3CKrIGY>vLH0v!51+USS`A\\-&nn~<R[E~)>Dw6:gyQTutyma7Z~dE#eF]Ge|jM 5{O<[0z2>[5(-Q/R9{",
        )
        self.assertEqual(test_model.id, 1)
        self.assertEqual(
            test_model.email,
            "lmpNzAn@iAW43-Sj]8\"x*7ag#D'Fl&3i%tz'xNd(GM&k48UCfb3`@xFHUMTxlxl@#1hx);!-/Qkq(:mjXIAX'R-FF[CmyfS*c9}~3PR#=2]g=9DBENDWiSXX9h&r=O+oK};;;C6.Dtr{p+gYh+1*xL|-vl)x3CKrIGY>vLH0v!51+USS`A\\-&nn~<R[E~)>Dw6:gyQTutyma7Z~dE#eF]Ge|jM 5{O<[0z2>[5(-Q/R9{",
        )

    def test_user_required_fields_missing(self):
        # Assert User class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = User()


if __name__ == "__main__":
    unittest.main()
