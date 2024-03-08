from .base import BaseModel


class ApiToken(BaseModel):
    """
    An API token to use for authentication.
    """

    def __init__(self, access_token: str, token_type: str = None, **kwargs):
        """
        Initialize ApiToken
        Parameters:
        ----------
            access_token: str
                The bearer token to use with the API. Pass this in the Authorization header as a bearer token.
            token_type: str
                The type of token. This will always be bearer.
        """
        self.access_token = access_token
        self.token_type = token_type
