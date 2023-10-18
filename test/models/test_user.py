import unittest
from src.llamastore.models.User import User


class TestUserModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_user(self):
        # Create User class instance
        test_model = User(
            id=8,
            email="wt\\Df@=ick.*9b_G, RV1Z1bywoTBBE$q-6[lluz23Fv=S=.$]>VT^[bqyBc.ceB\\Z4@})brBGWO_j*I5GFYX VtflV.`fC1JB5 cC~",
        )
        self.assertEqual(test_model.id, 8)
        self.assertEqual(
            test_model.email,
            "wt\\Df@=ick.*9b_G, RV1Z1bywoTBBE$q-6[lluz23Fv=S=.$]>VT^[bqyBc.ceB\\Z4@})brBGWO_j*I5GFYX VtflV.`fC1JB5 cC~",
        )

    def test_user_required_fields_missing(self):
        # Assert User class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = User()


if __name__ == "__main__":
    unittest.main()
