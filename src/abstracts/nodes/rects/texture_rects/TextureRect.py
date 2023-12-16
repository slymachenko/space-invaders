from abc import ABC
import pygame

# CUSTOM MODULES
from src.utils import constants as const

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


    def __init__(
            self, 
            renderer : Renderer, 
            x : int, 
            y : int, 
            width : int, 
            height : int, 
            path : str, 
            rect_mode : int = const.CORNER, 
            wrap_mode : int = const.CORNER
    ):
        super().__init__(renderer, x, y, width, height)
        self.path = path
        self.rect_mode = rect_mode
        self.wrap_mode = wrap_mode
        self.tiles_x = 1
        self.tiles_y = 1
        self.img = pygame.image.load(self.path)
    
    def wrap_mode_setup(self) -> None:
        pass

    def rect_mode_setup(self) -> None:
        pass