from enum import Enum


class LlamaColor(Enum):
    """
    The color of a llama.
    """

    BROWN = "brown"
    WHITE = "white"
    BLACK = "black"
    GRAY = "gray"

    def list():
        return list(map(lambda x: x.value, LlamaColor._member_map_.values()))
