from src.utils import constants as const

# BASES
from src.bases.nodes.Sprite import Sprite
from src.bases.Updateable import Updateable

# TYPES
from typing import List
from src.bases.scenes.Scene import Scene


class Projectile(Sprite, Updateable):
    speed: int
    direction: List[int]  # [x: int, y: int]

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
        direction: List[int] = [0, 0],
    ):
        super().__init__(scene, x, y, width, height, path, rect_mode, wrap_mode)
        self.speed = speed
        self.direction = direction

    def update(self) -> None:
        pass
