from src.utils import constants as const

# BASES
from src.bases.nodes.AnimatedSprite import AnimatedSprite
from src.bases.Inputable import Inputable

# TYPES
from src.bases.scenes.Scene import Scene


class Button(AnimatedSprite, Inputable):
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
    ):
        super().__init__(scene, x, y, width, height, path, rect_mode, wrap_mode)
