from pygame.locals import K_LEFT, K_RIGHT, K_SPACE

# CUSTOM MODULES
from src.utils import constants as const

# ABSTRACTS
from src.modules.nodes.rects.texture_rects.StaticTextureRect import StaticTextureRect
from src.abstracts.nodes.rects.texture_rects.entities.Entity import Entity

# TYPES
from typing import Tuple
from src.core.Renderer import Renderer
from src.core.InputHandler import InputHandler
from src.core.Updater import Updater
from pygame.rect import Rect


class PlayerEntity(StaticTextureRect, Entity):
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
        wrap_mode: int = const.CORNER,
    ):
        super().__init__(renderer, x, y, width, height, path, rect_mode, wrap_mode)
        self.input_handler = input_handler
        self.updater = updater
        self.rect = self.img.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.speed = 10

    def input(self) -> None:
        if self.input_handler.keys[K_LEFT]:
            self.move((-1, 0))
        if self.input_handler.keys[K_RIGHT]:
            self.move((1, 0))
        if self.input_handler.keys[K_SPACE]:
            print("SPACE")

    def update(self) -> None:
        pass

    def move(self, vec: tuple()) -> None:
        match vec[0]:
            case 1:
                self.x += self.speed
            case -1:
                self.x -= self.speed

        match vec[1]:
            case 1:
                self.y += self.speed
            case -1:
                self.y -= self.speed
