from abc import ABC

# CUSTOM MODULES
from src.utils import constants as const

# ABSTRACTS
from src.abstracts.nodes.rects.texture_rects.TextureRect import TextureRect
from src.abstracts.Updateable import Updateable

# TYPES
from typing import Tuple
from src.abstracts.scenes.Scene import Scene
from pygame import Surface as PySurface
from pygame import Rect as PyRect


class Entity(TextureRect, Updateable, ABC):
    sprite: PySurface
    sprite_size: Tuple[int, int]
    rect: PyRect
    speed: Tuple[int, int]

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
        speed: Tuple[int, int] = (10, 10),
    ):
        super().__init__(scene, x, y, width, height, path, rect_mode, wrap_mode)
        self.speed = speed
        self.sprite = self.img
        self.sprite_size = self.sprite.get_size()

    def input(self) -> None:
        pass

    def update(self) -> None:
        pass

    def move(self) -> None:
        pass

    def handle_borders(self) -> None:
        pass
