from src.utils import constants as const

# BASES
from src.bases.nodes.AnimatedSprite import AnimatedSprite

# TYPES
from typing import Tuple
from src.bases.scenes.Scene import Scene


class Entity(AnimatedSprite):
    speed: Tuple[int, int]

    def __init__(
        self,
        scene: Scene,
        x: int,
        y: int,
        width: int,
        height: int,
        path: str,
        num_frames: int,
        rect_mode: int = const.CORNER,
        wrap_mode: int = const.CLAMP,
        speed: Tuple[int, int] = (10, 10),
    ):
        super().__init__(
            scene, x, y, width, height, path, num_frames, rect_mode, wrap_mode
        )
        self.speed = speed

    def move(self, vec: Tuple[int, int]) -> None:
        match vec[0]:
            case 1:
                self.x += self.speed[0]
            case -1:
                self.x -= self.speed[0]

        match vec[1]:
            case 1:
                self.y += self.speed[1]
            case -1:
                self.y -= self.speed[1]
