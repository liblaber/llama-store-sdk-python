import unittest
from src.llamastore.models.RegisterUserRequest import RegisterUserRequest


class TestRegisterUserRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_register_user_request(self):
        # Create RegisterUserRequest class instance
        test_model = RegisterUserRequest(
            password="architecto",
            email='b7+`>R53f$+peew]zd:wR(p<yn["\\4c/Mb@#_?nR[7+3[T"w/x[<lf.;@o3\\%:H)u.@0<790.K9uR~>44qiC;E-?y_)G_$5vYoUD|$N&K>h{ohY14h>*j~Hjofp"=q~]Z5Y2\'-V__\'S&VNPm7-A/q?xQ#+V}w<yn=-$TdoUDf=C',
        )
        self.assertEqual(test_model.password, "architecto")
        self.assertEqual(
            test_model.email,
            'b7+`>R53f$+peew]zd:wR(p<yn["\\4c/Mb@#_?nR[7+3[T"w/x[<lf.;@o3\\%:H)u.@0<790.K9uR~>44qiC;E-?y_)G_$5vYoUD|$N&K>h{ohY14h>*j~Hjofp"=q~]Z5Y2\'-V__\'S&VNPm7-A/q?xQ#+V}w<yn=-$TdoUDf=C',
        )

    def test_register_user_request_required_fields_missing(self):
        # Assert RegisterUserRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = RegisterUserRequest()


if __name__ == "__main__":
    unittest.main()
