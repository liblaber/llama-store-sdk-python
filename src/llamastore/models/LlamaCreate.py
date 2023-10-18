from .base import BaseModel
from .LlamaColor import LlamaColor


class LlamaCreate(BaseModel):
    """
    A new llama for the llama store.
    """

    def __init__(self, rating: int, color: LlamaColor, age: int, name: str, **kwargs):
        """
        Initialize LlamaCreate
        Parameters:
        ----------
            rating: int
            color: LlamaColor
            age: int
            name: str
        """
        self.rating = rating
        self.color = self._enum_matching(color, LlamaColor.list(), "color")
        self.age = age
        self.name = name
