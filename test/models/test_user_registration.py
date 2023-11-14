import unittest
from src.llamastore.models.UserRegistration import UserRegistration


class TestUserRegistrationModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_user_registration(self):
        # Create UserRegistration class instance
        test_model = UserRegistration(
            password="quis",
            email="uW04}0zB%id|]s,E;v-]2i[?\\T.4OI~Q_)@vK8LVQqxI4(qP'2y13^bw().a7`l]25O&@'Ca4QzqqY`W)\"El%U'i>BN?  @&oTyiSI33zgr0XKwgtn!P\"$hHInUHN|eflc[LH0|'.D949,i49(l-ht{4k.j[QO}#c'Byym8N3N@c-]4o,;x46cV\"zf6^J:hs>THHJ7I@{",
        )
        self.assertEqual(test_model.password, "quis")
        self.assertEqual(
            test_model.email,
            "uW04}0zB%id|]s,E;v-]2i[?\\T.4OI~Q_)@vK8LVQqxI4(qP'2y13^bw().a7`l]25O&@'Ca4QzqqY`W)\"El%U'i>BN?  @&oTyiSI33zgr0XKwgtn!P\"$hHInUHN|eflc[LH0|'.D949,i49(l-ht{4k.j[QO}#c'Byym8N3N@c-]4o,;x46cV\"zf6^J:hs>THHJ7I@{",
        )

    def test_user_registration_required_fields_missing(self):
        # Assert UserRegistration class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UserRegistration()


if __name__ == "__main__":
    unittest.main()
