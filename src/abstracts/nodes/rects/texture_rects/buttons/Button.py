from abc import ABC

# CUSTOM MODULES
from src.utils import constants as const

# ABSTRACTS
from src.abstracts.nodes.rects.texture_rects.TextureRect import TextureRect
from src.abstracts.Inputable import Inputable
from src.abstracts.Updateable import Updateable

# TYPES
from src.abstracts.scenes.Scene import Scene
from pygame.rect import Rect


class Button(TextureRect, Inputable, Updateable, ABC):
    rect: Rect

    def __init__(
        self,
        scene: Scene,
        x: int,
        y: int,
        width: int,
        height: int,
        path: str,
        target_scene: Scene,
        rect_mode: int = const.CORNER,
        wrap_mode: int = const.CLAMP,
    ):
        super().__init__(scene, x, y, width, height, path, rect_mode, wrap_mode)

        self.target_scene = target_scene

    def input(self) -> None:
        pass

    def update(self) -> None:
        pass
