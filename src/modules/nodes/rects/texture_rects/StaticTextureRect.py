import pygame
import math

# CUSTOM MODULES
from src.utils import constants as const

# ABSTRACT
from src.abstracts.nodes.rects.texture_rects.TextureRect import TextureRect

# TYPES
from typing import Tuple
from pygame.surface import Surface
from src.abstracts.scenes.Scene import Scene


class StaticTextureRect(TextureRect):
    scene: Scene
    x: int
    y: int
    width: int
    height: int
    path: str
    rect_mode: int
    wrap_mode: int
    img: Surface
    tiles_x: int
    tiles_y: int

    def __init__(
        self,
        scene: Scene,
        x: int,
        y: int,
        width: int,
        height: int,
        path: str,
        rect_mode: int = const.CORNER,
        wrap_mode: int = const.CORNER,
    ):
        super().__init__(scene, x, y, width, height, path, rect_mode, wrap_mode)
        self.rect_mode_setup()
        self.wrap_mode_setup()

    def wrap_mode_setup(self) -> None:
        img_size_new: Tuple(int, int)
        aspect_ratio: float

        img_size: Tuple(int, int) = self.img.get_size()

        match self.wrap_mode:
            case const.REPEAT:
                self.tiles_x = math.ceil(self.width / img_size[0])
                self.tiles_y = math.ceil(self.height / img_size[1])
            case const.CLAMP:
                aspect_ratio = img_size[0] / img_size[1]

                if self.width > self.height:
                    img_size_new = (self.width, int(self.width / aspect_ratio))
                else:
                    img_size_new = (int(self.height * aspect_ratio), self.height)

                self.img = pygame.transform.scale(self.img, img_size_new)
            case const.STRETCH:
                img_size_new = (
                    math.ceil(img_size[0] * self.width / img_size[0]),
                    math.ceil(img_size[1] * self.height / img_size[1]),
                )

                self.img = pygame.transform.scale(self.img, img_size_new)

    def rect_mode_setup(self) -> None:
        match self.rect_mode:
            case const.CORNER:
                pass
            case const.CENTER:
                self.x -= self.width // 2
                self.y -= self.height // 2

    def render(self) -> None:
        img_size = self.img.get_size()
        for x in range(self.tiles_x):
            for y in range(self.tiles_y):
                self.scene.renderer.screen.blit(
                    self.img, (self.x + x * img_size[0], self.y + y * img_size[1])
                )
