from .base import BaseModel


class ApiTokenRequest(BaseModel):
    """
    A request to get an API token for a given user.
    """

    def __init__(self, password: str, email: str, **kwargs):
        """
        Initialize ApiTokenRequest
        Parameters:
        ----------
            password: str
            email: str
        """
        self.password = password
        self.email = email
