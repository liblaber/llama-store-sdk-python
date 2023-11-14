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
                The password of the user. This must be at least 8 characters long, and contain at least one letter, one number, and one special character.
            email: str
                The email address of the user. This must be unique across all users.
        """
        self.password = password
        self.email = self._pattern_matching(email, ".+\@.+\..+", "email")
