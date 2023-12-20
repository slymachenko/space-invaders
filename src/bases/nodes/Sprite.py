from math import ceil
from pygame.image import load
from pygame.transform import scale
from src.utils import constants as const

# BASES
from src.bases.nodes.Node import Node
from src.bases.Renderable import Renderable

# TYPES
from typing import Tuple
from pygame.surface import Surface
from src.bases.scenes.Scene import Scene


class Sprite(Node, Renderable):
    scene: Scene
    x: int
    y: int
    width: int
    height: int
    path: str
    rect_mode: int
    wrap_mode: int

    sprite: Surface
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
        wrap_mode: int = const.REPEAT,
    ):
        super().__init__(scene, x, y, width, height)
        self.path = path
        self.rect_mode = rect_mode
        self.wrap_mode = wrap_mode

        self.sprite = load(self.path)
        self.tiles_x = 1
        self.tiles_y = 1

        self.wrap_mode_setup()
        self.rect_mode_setup()

    def wrap_mode_setup(self) -> None:
        img_size_new: Tuple[int, int]
        aspect_ratio: float

        img_size: Tuple[int, int] = self.sprite.get_size()

        match self.wrap_mode:
            case const.REPEAT:
                self.tiles_x = ceil(self.width / img_size[0])
                self.tiles_y = ceil(self.height / img_size[1])

            case const.CLAMP:
                aspect_ratio = img_size[0] / img_size[1]

                if self.width > self.height:
                    img_size_new = (self.width, int(self.width / aspect_ratio))
                else:
                    img_size_new = (int(self.height * aspect_ratio), self.height)

                self.sprite = scale(self.sprite, img_size_new)

            case const.STRETCH:
                img_size_new = (
                    ceil(img_size[0] * self.width / img_size[0]),
                    ceil(img_size[1] * self.height / img_size[1]),
                )

                self.sprite = scale(self.sprite, img_size_new)

    def rect_mode_setup(self) -> None:
        match self.rect_mode:
            case const.CORNER:
                pass

            case const.CENTER:
                self.x -= self.width // 2
                self.y -= self.height // 2
                self.rect.topleft = (self.x, self.y)

    def render(self) -> None:
        img_size: Tuple[int, int] = self.sprite.get_size()

        for x in range(self.tiles_x):
            for y in range(self.tiles_y):
                self.scene.renderer.screen.blit(
                    self.sprite, (self.x + x * img_size[0], self.y + y * img_size[1])
                )
