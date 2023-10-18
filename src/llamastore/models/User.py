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
            email: str
        """
        self.id = id
        self.email = self._pattern_matching(email, ".+\@.+\..+", "email")
