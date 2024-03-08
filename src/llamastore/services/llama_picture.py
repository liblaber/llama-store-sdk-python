from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.LlamaId import LlamaId as LlamaIdModel


class LlamaPicture(BaseService):
    def get_llama_picture_by_llama_id(self, llama_id: int):
        """
        Get Llama Picture
        Parameters:
        ----------
            llama_id: int
                The ID of the llama to get the picture for
        """

        url_endpoint = "/llama/{llama_id}/picture"
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
        return res

    def create_llama_picture(
        self, llama_id: int, request_input: str = None
    ) -> LlamaIdModel:
        """
        Create Llama Picture
        Parameters:
        ----------
            llama_id: int
                The ID of the llama that this picture is for
        """

        url_endpoint = "/llama/{llama_id}/picture"
        headers = {"Content-Type": "image/png"}
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
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return LlamaIdModel(**res)
        return res

    def update_llama_picture(
        self, llama_id: int, request_input: str = None
    ) -> LlamaIdModel:
        """
        Update Llama Picture
        Parameters:
        ----------
            llama_id: int
                The ID of the llama that this picture is for
        """

        url_endpoint = "/llama/{llama_id}/picture"
        headers = {"Content-Type": "image/png"}
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
            return LlamaIdModel(**res)
        return res

    def delete_llama_picture(self, llama_id: int):
        """
        Delete Llama Picture
        Parameters:
        ----------
            llama_id: int
                The ID of the llama to delete the picture for
        """

        url_endpoint = "/llama/{llama_id}/picture"
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
