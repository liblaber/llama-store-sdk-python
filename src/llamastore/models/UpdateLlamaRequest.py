from .base import BaseModel
from .LlamaColor import LlamaColor


class UpdateLlamaRequest(BaseModel):
    """
    A new llama for the llama store.
    """

    def __init__(self, rating: int, color: LlamaColor, age: int, name: str, **kwargs):
        """
        Initialize UpdateLlamaRequest
        Parameters:
        ----------
            rating: int
                The rating of the llama from 1 to 5.
            color: LlamaColor
            age: int
                The age of the llama in years.
            name: str
                The name of the llama. This must be unique across all llamas.
        """
        self.rating = rating
        self.color = self._enum_matching(color, LlamaColor.list(), "color")
        self.age = age
        self.name = name
