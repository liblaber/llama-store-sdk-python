from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.User import User as UserModel
from ..models.UserRegistration import UserRegistration as UserRegistrationModel


class User(BaseService):
    def get_user_by_email(self, email: str) -> UserModel:
        """
        Get User By Email
        Parameters:
        ----------
            email: str
                The user's email address
        """

        url_endpoint = "/user/{email}"
        headers = {}
        self._add_required_headers(headers)
        if not email:
            raise ValueError("Parameter email is required, cannot be empty or blank.")
        validated_email = self._pattern_matching(email, ".+\@.+\..+", "email")
        url_endpoint = url_endpoint.replace(
            "{email}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, validated_email, None
                    )
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return UserModel(**res)
        return res

    def register_user(self, request_input: UserRegistrationModel) -> UserModel:
        """
        Register User
        """

        url_endpoint = "/user"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return UserModel(**res)
        return res
