import unittest
from src.llamastore.models.User import User


class TestUserModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_user(self):
        # Create User class instance
        test_model = User(
            id=2,
            email='AKjfeS0)s90nS1l(jN)-x*z$X/c@{ZD,*Lh=1%J{NT4OD5@k6Mg)T\\#S+w)iu9:)ODmG0nS`5wM[:r}%\\O5+2h!H0e9l>W3A;?,}S7t$Y~|$sE.y+jTRmLB^O(NP/J"B2vt5gc?M',
        )
        self.assertEqual(test_model.id, 2)
        self.assertEqual(
            test_model.email,
            'AKjfeS0)s90nS1l(jN)-x*z$X/c@{ZD,*Lh=1%J{NT4OD5@k6Mg)T\\#S+w)iu9:)ODmG0nS`5wM[:r}%\\O5+2h!H0e9l>W3A;?,}S7t$Y~|$sE.y+jTRmLB^O(NP/J"B2vt5gc?M',
        )

    def test_user_required_fields_missing(self):
        # Assert User class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = User()


if __name__ == "__main__":
    unittest.main()
