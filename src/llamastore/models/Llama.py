from .base import BaseModel
from .LlamaColor import LlamaColor


class Llama(BaseModel):
    """
    A llama, with details of its name, age, color, and rating from 1 to 5.
    """

    def __init__(
        self, id: int, rating: int, color: LlamaColor, age: int, name: str, **kwargs
    ):
        """
        Initialize Llama
        Parameters:
        ----------
            id: int
                The ID of the llama.
            rating: int
                The rating of the llama from 1 to 5.
            color: LlamaColor
            age: int
                The age of the llama in years.
            name: str
                The name of the llama. This must be unique across all llamas.
        """
        self.id = id
        self.rating = rating
        self.color = self._enum_matching(color, LlamaColor.list(), "color")
        self.age = age
        self.name = name
