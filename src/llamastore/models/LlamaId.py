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
                The ID of the llama.
        """
        self.id = id
