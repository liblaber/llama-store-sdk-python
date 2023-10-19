import unittest
from src.llamastore.models.User import User


class TestUserModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_user(self):
        # Create User class instance
        test_model = User(
            id=8,
            email=",']!K#3@>.KHC'XG'8RFIuYc|91\\W'xU~?q[^gBR<E![mL33u~LTr'cB-a,:dR7p@AART~N;uIA5UkWJ'&3RR,D}1_&3,E2)LY&X1HOlR,9SS&--.3}.sOSU~'SM`!'Ko],%~/Q}*d5}H5cRcBh~?jd:GAw!;#gH[ A}8N24#v%-Edf)cR/,(BVYs8otXH3}8",
        )
        self.assertEqual(test_model.id, 8)
        self.assertEqual(
            test_model.email,
            ",']!K#3@>.KHC'XG'8RFIuYc|91\\W'xU~?q[^gBR<E![mL33u~LTr'cB-a,:dR7p@AART~N;uIA5UkWJ'&3RR,D}1_&3,E2)LY&X1HOlR,9SS&--.3}.sOSU~'SM`!'Ko],%~/Q}*d5}H5cRcBh~?jd:GAw!;#gH[ A}8N24#v%-Edf)cR/,(BVYs8otXH3}8",
        )

    def test_user_required_fields_missing(self):
        # Assert User class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = User()


if __name__ == "__main__":
    unittest.main()
