import unittest
from src.llamastore.models.User import User


class TestUserModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_user(self):
        # Create User class instance
        test_model = User(
            id=9,
            email='e#[RBr1KNs~{GA\'/Qp >g!"M]!FS/42[b*WW~KP=sLT%."J\'J6&:9f@KF<[?YIFUJ*$@e:(Nk!#Mf_gu\\>iJf4.:n]5\\B(9>|Lm\\s)F^x1q4q>s$JHLpA&Hx" g&h2qw$A6Z)yRpvQ8)h:l^r9D75S8',
        )
        self.assertEqual(test_model.id, 9)
        self.assertEqual(
            test_model.email,
            'e#[RBr1KNs~{GA\'/Qp >g!"M]!FS/42[b*WW~KP=sLT%."J\'J6&:9f@KF<[?YIFUJ*$@e:(Nk!#Mf_gu\\>iJf4.:n]5\\B(9>|Lm\\s)F^x1q4q>s$JHLpA&Hx" g&h2qw$A6Z)yRpvQ8)h:l^r9D75S8',
        )

    def test_user_required_fields_missing(self):
        # Assert User class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = User()


if __name__ == "__main__":
    unittest.main()
