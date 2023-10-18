from .base import BaseModel


class UserRegistration(BaseModel):
    """
    A new user of the llama store.
    """

    def __init__(self, password: str, email: str, **kwargs):
        """
        Initialize UserRegistration
        Parameters:
        ----------
            password: str
            email: str
        """
        self.password = password
        self.email = self._pattern_matching(email, ".+\@.+\..+", "email")
