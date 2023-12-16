from abc import ABC

# ABSTRACT
from src.abstracts.nodes.rects.Rect import Rect

# TYPES
from src.core.Renderer import Renderer


class TextureRect(Rect, ABC):
    color: list[int, int, int]

    def __init__(self, renderer: Renderer, x: int, y: int, width: int, height: int):
        super().__init__(renderer, x, y, width, height)
