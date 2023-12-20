from src.utils import constants as const

# BASES
from src.bases.nodes.Entity import Entity
from src.bases.Inputable import Inputable
from src.nodes.projectiles.PlayerProjectile import (
    PlayerProjectile,
)

# TYPES
from typing import Tuple
from src.bases.scenes.Scene import Scene
from pygame.rect import Rect


class PlayerEntity(Entity, Inputable):
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
        speed: Tuple[int, int] = (10, 10),
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
        if self.scene.input_manager.events["left"]:
            self.move((-1, 0))
        if self.scene.input_manager.events["right"]:
            self.move((1, 0))
        if self.scene.input_manager.events["shoot"]:
            self.shoot()

    def update(self) -> None:
        self.handle_borders()

    def handle_borders(self) -> None:
        game_screen_x: Tuple[int, int] = self.scene.updater.game_screen_x
        sprite_size: Tuple[int, int] = self.sprite.get_size()

        if self.x < game_screen_x[0]:
            self.x = game_screen_x[0]
        elif self.x > game_screen_x[1] - sprite_size[0]:
            self.x = game_screen_x[1] - sprite_size[0]

    def shoot(self):
        if not self.scene.check_node(self.bullet):
            self.gen_bullet()
            self.scene.nodes.append(self.bullet)

    def gen_bullet(self) -> None:
        sprite_size = self.sprite.get_size()
        self.bullet = PlayerProjectile(
            self.scene,
            self.x + sprite_size[0] / 2,
            self.y,
            2,
            1,
            "assets/imgs/bullet1.png",
            rect_mode=const.CENTER,
            wrap_mode=const.CLAMP,
            speed=15,
        )
