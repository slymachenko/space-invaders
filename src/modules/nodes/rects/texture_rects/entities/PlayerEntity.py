# CUSTOM MODULES
from src.utils import constants as const

# ABSTRACTS
from src.modules.nodes.rects.texture_rects.StaticTextureRect import StaticTextureRect
from src.abstracts.nodes.rects.texture_rects.entities.Entity import Entity
from src.modules.nodes.rects.texture_rects.projectiles.PlayerProjectile import (
    PlayerProjectile,
)

# TYPES
from typing import Tuple
from src.abstracts.scenes.Scene import Scene
from pygame.rect import Rect


class PlayerEntity(Entity, StaticTextureRect):
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
        super().__init__(
            scene,
            x,
            y,
            width,
            height,
            path,
            rect_mode,
            wrap_mode,
            speed,
        )

        self.gen_bullet()

    def input(self) -> None:
        if self.scene.input_handler.events["left"]:
            self.move((-1, 0))
        if self.scene.input_handler.events["right"]:
            self.move((1, 0))
        if self.scene.input_handler.events["shoot"]:
            self.shoot()

    def update(self) -> None:
        self.handle_borders()

    def move(self, vec: Tuple[int, int]) -> None:
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

    def handle_borders(self) -> None:
        game_screen_x: Tuple[int, int] = self.scene.updater.game_screen_x
        img_size: Tuple[int, int] = self.img.get_size()

        if self.x < game_screen_x[0]:
            self.x = game_screen_x[0]
        elif self.x > game_screen_x[1] - img_size[0]:
            self.x = game_screen_x[1] - img_size[0]

    def shoot(self):
        if not self.scene.check_node(self.bullet):
            self.gen_bullet()
            self.scene.nodes.append(self.bullet)

    def gen_bullet(self) -> None:
        img_size = self.img.get_size()
        self.bullet = PlayerProjectile(
            self.scene,
            self.x + img_size[0] / 2,
            self.y,
            2,
            1,
            "assets/bullet1.png",
            rect_mode=const.CENTER,
            wrap_mode=const.CLAMP,
            speed=15,
        )
