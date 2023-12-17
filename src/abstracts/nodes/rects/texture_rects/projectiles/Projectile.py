from abc import ABC

# CUSTOM MODULES
from src.utils import constants as const

# ABSTRACTS
from src.abstracts.nodes.rects.texture_rects.TextureRect import TextureRect
from src.abstracts.Updateable import Updateable

# TYPES
from src.abstracts.scenes.Scene import Scene
from pygame import Rect


class Projectile(TextureRect, Updateable, ABC):
    rect: Rect
    speed: int

    def __init__(
        self,
        scene: Scene,
        x: int,
        y: int,
        width: int,
        height: int,
        path: str,
        rect_mode: int = const.CORNER,
        wrap_mode: int = const.CLAMP,
        speed: int = 10,
    ):
        super().__init__(scene, x, y, width, height, path, rect_mode, wrap_mode)
        self.speed = speed
        self.rect = self.img.get_rect()
        self.rect.topleft = (self.x, self.y)

    def update(self) -> None:
        pass
