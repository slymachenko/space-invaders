from src.utils import constants as const

# BASES
from src.bases.nodes.Entity import Entity
from src.nodes.projectiles.PlayerProjectile import (
    PlayerProjectile,
)

# TYPES
from typing import Tuple
from src.bases.scenes.Scene import Scene


class AlienEntity(Entity):
    direction: list[int]
    animate_step: int

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
        direction: list[int] = [1, 0],
        wait_time: int = 10,
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

        self.direction = direction
        self.wait_time = wait_time

        self.setup()

    def setup(self) -> None:
        # self.img = self.sprite.subsurface(
        #     (0, 0, self.sprite_size[0] / 2, self.sprite_size[1])
        # )
        # self.rect = self.img.get_rect(topleft=(self.x, self.y))
        # self.animate_step = 0
        # self.step_timer = self.scene.renderer.ticks
        self.gen_bullet()

    def update(self) -> None:
        pass
        # now = self.scene.renderer.ticks
        # if now - self.step_timer >= self.wait_time:
        #     self.snake_move()
        #     self.animate()

        #     self.step_timer = now

        # self.handle_borders()
        # self.rect.topleft = (self.x, self.y)

    def snake_move(self) -> None:
        self.move(self.direction)

        if self.direction[1] == 1:
            self.direction[1] = 0

    def animate(self) -> None:
        match self.animate_step:
            case 0:
                self.img = self.sprite.subsurface(
                    (
                        self.sprite_size[0] // 2,
                        0,
                        self.sprite_size[0] // 2,
                        self.sprite_size[1],
                    )
                )
                self.animate_step = 1
            case 1:
                self.img = self.sprite.subsurface(
                    (0, 0, self.sprite_size[0] / 2, self.sprite_size[1])
                )
                self.animate_step = 0

    def handle_borders(self) -> None:
        game_screen_x: Tuple[int, int] = self.scene.updater.game_screen_x
        game_screen_y: Tuple[int, int] = self.scene.updater.game_screen_y

        if self.x < game_screen_x[0]:
            self.x = game_screen_x[0]
            self.direction[0] = 1
            self.direction[1] = 1
        elif self.x > game_screen_x[1] - self.img_size[0]:
            self.x = game_screen_x[1] - self.img_size[0]
            self.direction[0] = -1
            self.direction[1] = 1

        if self.y < game_screen_y[0]:
            self.y = game_screen_y[0]
            self.direction[1] = 1
        elif self.y > game_screen_y[1] - self.img_size[1]:
            self.y = game_screen_y[1] - self.img_size[1]
            self.direction[1] = -1

    def shoot(self) -> None:
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
