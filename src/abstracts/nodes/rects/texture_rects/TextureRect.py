from abc import ABC

# ABSTRACT
from src.abstracts.nodes.rects.Rect import Rect

# TYPES
from src.core.Renderer import Renderer
from pygame import Surface

class TextureRect(Rect, ABC):
    path : str
    rect_mode : int
    wrap_mode : int
    img : Surface
    tiles_x : int
    tiles_y : int


    def __init__(self, renderer : Renderer, x : int, y : int, width : int, height : int):
        super().__init__(renderer, x, y, width, height)
    
    def wrap_mode_setup(self) -> None:
        pass

    def rect_mode_setup(self) -> None:
        pass