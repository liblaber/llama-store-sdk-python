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
            token_type: str
        """
        self.access_token = access_token
        self.token_type = token_type
