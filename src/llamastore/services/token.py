from urllib.parse import quote

from .base import BaseService
from ..models.CreateApiTokenRequest import (
    CreateApiTokenRequest as CreateApiTokenRequestModel,
)
from ..models.ApiToken import ApiToken as ApiTokenModel


class Token(BaseService):
    def create_api_token(
        self, request_input: CreateApiTokenRequestModel
    ) -> ApiTokenModel:
        """
        Create Api Token
        """

        url_endpoint = "/token"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return ApiTokenModel(**res)
        return res
