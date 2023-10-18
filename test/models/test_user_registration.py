import unittest
from src.llamastore.models.UserRegistration import UserRegistration


class TestUserRegistrationModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_user_registration(self):
        # Create UserRegistration class instance
        test_model = UserRegistration(
            password="deserunt",
            email='TsNCdofR-hiMr#\'-/:gG]Cc}v<c8t1$\\r e8(H|AMv$)~S-HB_ggMz/-[gCVyma1"@L!oq1Gga<u6rwhp\\-.bj+iRDK!)CjTJ$?.cP}4d->@$;"T@t0p{K00Gdap ;+9?1@==7\\n/kU%E2zdIZrzUu"Cf0mgO&i|.-2US6[8-3/g"%2P',
        )
        self.assertEqual(test_model.password, "deserunt")
        self.assertEqual(
            test_model.email,
            'TsNCdofR-hiMr#\'-/:gG]Cc}v<c8t1$\\r e8(H|AMv$)~S-HB_ggMz/-[gCVyma1"@L!oq1Gga<u6rwhp\\-.bj+iRDK!)CjTJ$?.cP}4d->@$;"T@t0p{K00Gdap ;+9?1@==7\\n/kU%E2zdIZrzUu"Cf0mgO&i|.-2US6[8-3/g"%2P',
        )

    def test_user_registration_required_fields_missing(self):
        # Assert UserRegistration class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UserRegistration()


if __name__ == "__main__":
    unittest.main()
