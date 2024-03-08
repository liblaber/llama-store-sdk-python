import unittest
from src.llamastore.models.CreateApiTokenRequest import CreateApiTokenRequest


class TestCreateApiTokenRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_create_api_token_request(self):
        # Create CreateApiTokenRequest class instance
        test_model = CreateApiTokenRequest(
            password="accusantium",
            email="\"hqE`p:[Rq<B2B@I%A}1/?MDQQ&(v;Q&YPFCz~ySMF&firhmU@SJUE<8G<Wds^B80X=p'm^glrd{JpkLY$<\\55 +h:&ylbxBN^E)-b8&D@5u5.OS=0k5QA/lf:gRn\\/FSb80ClotH)=bJRu",
        )
        self.assertEqual(test_model.password, "accusantium")
        self.assertEqual(
            test_model.email,
            "\"hqE`p:[Rq<B2B@I%A}1/?MDQQ&(v;Q&YPFCz~ySMF&firhmU@SJUE<8G<Wds^B80X=p'm^glrd{JpkLY$<\\55 +h:&ylbxBN^E)-b8&D@5u5.OS=0k5QA/lf:gRn\\/FSb80ClotH)=bJRu",
        )

    def test_create_api_token_request_required_fields_missing(self):
        # Assert CreateApiTokenRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = CreateApiTokenRequest()


if __name__ == "__main__":
    unittest.main()
