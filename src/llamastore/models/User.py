from .base import BaseModel


class User(BaseModel):
    """
    A user of the llama store
    """

    def __init__(self, id: int, email: str, **kwargs):
        """
        Initialize User
        Parameters:
        ----------
            id: int
                The ID of the user. This is unique across all users.
            email: str
                The email address of the user. This must be unique across all users.
        """
        self.id = id
        self.email = self._pattern_matching(email, ".+\@.+\..+", "email")
