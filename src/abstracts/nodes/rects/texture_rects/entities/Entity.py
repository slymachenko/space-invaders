from abc import ABC

# CUSTOM MODULES
from src.utils import constants as const

# ABSTRACTS
from src.abstracts.nodes.rects.texture_rects.TextureRect import TextureRect
from src.abstracts.Inputable import Inputable
from src.abstracts.Updateable import Updateable

# TYPES
from src.core.Renderer import Renderer
from src.core.InputHandler import InputHandler
from src.core.Updater import Updater
from pygame import Rect


class Entity(TextureRect, Inputable, Updateable, ABC):
    rect: Rect
    speed: int

    def __init__(
        self,
        renderer: Renderer,
        input_handler: InputHandler,
        updater: Updater,
        x: int,
        y: int,
        width: int,
        height: int,
        path: str,
        rect_mode: int = const.CORNER,
        wrap_mode: int = const.CLAMP,
        speed: int = 10,
    ):
        super().__init__(renderer, x, y, width, height, path, rect_mode, wrap_mode)
        self.input_handler = input_handler
        self.updater = updater
        self.speed = speed
        self.rect = self.img.get_rect()
        self.rect.topleft = (self.x, self.y)

    def input(self) -> None:
        pass

    def update(self) -> None:
        pass

    def move(self) -> None:
        pass

    def handle_borders(self) -> None:
        pass
