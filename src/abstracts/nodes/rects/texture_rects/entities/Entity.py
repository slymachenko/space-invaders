from abc import ABC

# CUSTOM MODULES
from src.utils import constants as const

# ABSTRACTS
from src.abstracts.nodes.rects.texture_rects.TextureRect import TextureRect
from src.abstracts.Inputable import Inputable
from src.abstracts.Updateable import Updateable

# TYPES
from src.core.Renderer import Renderer

class Entity(TextureRect, Inputable, Updateable, ABC):
    def __init__(self, renderer : Renderer, x : int, y : int, width : int, height : int, path : str, rect_mode : int = const.CORNER, wrap_mode : int = const.CORNER):
        super().__init__(renderer, x, y, width, height, path, rect_mode, wrap_mode)
    
    def input(self) -> None:
        pass

    def update(self) -> None:
        pass