from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.GetLlamasResponse import GetLlamasResponse as GetLlamasResponseModel
from ..models.Llama import Llama as LlamaModel
from ..models.LlamaCreate import LlamaCreate as LlamaCreateModel


class Llama(BaseService):
    def get_llamas(self) -> GetLlamasResponseModel:
        """
        Get Llamas
        """

        url_endpoint = "/llama"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, list):
            return [LlamaModel(**model) for model in res]
        return res

    def create_llama(self, request_input: LlamaCreateModel) -> LlamaModel:
        """
        Create Llama
        """

        url_endpoint = "/llama"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return LlamaModel(**res)
        return res

    def get_llama_by_id(self, llama_id: int) -> LlamaModel:
        """
        Get Llama
        Parameters:
        ----------
            llama_id: int
                The llama's ID
        """

        url_endpoint = "/llama/{llama_id}"
        headers = {}
        self._add_required_headers(headers)
        if not llama_id:
            raise ValueError(
                "Parameter llama_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{llama_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, llama_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return LlamaModel(**res)
        return res

    def update_llama(
        self, request_input: LlamaCreateModel, llama_id: int
    ) -> LlamaModel:
        """
        Update Llama
        Parameters:
        ----------
            llama_id: int
                The llama's ID
        """

        url_endpoint = "/llama/{llama_id}"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)
        if not llama_id:
            raise ValueError(
                "Parameter llama_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{llama_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, llama_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.put(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return LlamaModel(**res)
        return res

    def delete_llama(self, llama_id: int):
        """
        Delete Llama
        Parameters:
        ----------
            llama_id: int
                The llama's ID
        """

        url_endpoint = "/llama/{llama_id}"
        headers = {}
        self._add_required_headers(headers)
        if not llama_id:
            raise ValueError(
                "Parameter llama_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{llama_id}",
            quote(
                str(query_serializer.serialize_path("simple", False, llama_id, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        return res
