from .base import BaseModel


class LlamaId(BaseModel):
    """
    A llama id.
    """

    def __init__(self, id: int, **kwargs):
        """
        Initialize LlamaId
        Parameters:
        ----------
            id: int
        """
        self.id = id
