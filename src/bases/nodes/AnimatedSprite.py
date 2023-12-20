from src.utils import constants as const

# BASES
from src.bases.nodes.Sprite import Sprite
from src.bases.Updateable import Updateable

# TYPES
from typing import Tuple
from pygame.surface import Surface
from src.bases.scenes.Scene import Scene


class AnimatedSprite(Sprite, Updateable):
    num_frames: int

    current_frame: int
    sprite_sheet: Surface
    sprite_size: Tuple[int, int]

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
    ):
        super().__init__(scene, x, y, width, height, path, rect_mode, wrap_mode)
        self.num_frames = num_frames

        self.current_frame = 0
        self.sprite_sheet = self.sprite
        # self.sprite = self.set_sprite()

    def update(self) -> None:
        pass
        # self.sprite = self.set_sprite()

    # def set_sprite(self) -> None:
    #     width: int = self.sprite_sheet.get_width() // self.num_frames
    #     height: int = self.sprite_sheet.get_height()
    #     x = self.current_frame * width
    #     y = 0

    #     self.sprite = Surface.
