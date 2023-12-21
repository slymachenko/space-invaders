from pygame import mixer
import random
from src.utils import constants as const

# BASES
from src.bases.nodes.Entity import Entity
from src.nodes.projectiles.AlienProjectile import (
    AlienProjectile,
)

# TYPES
from typing import Tuple
from src.bases.scenes.Scene import Scene


class AlienEntity(Entity):
    direction: list[int]

    def __init__(
        self,
        scene: Scene,
        x: int,
        y: int,
        path: str,
        direction: list[int] = [1, 0],
        wait_time: int = 10,
        shoot_chance: int = 0,
    ):
        super().__init__(
            scene,
            x,
            y,
            width=30,
            height=30,
            path=path,
            num_frames=2,
            rect_mode=const.CORNER,
            wrap_mode=const.CLAMP,
            speed=(10, 40),
        )

        self.direction = direction
        self.wait_time = wait_time
        self.shoot_chance = shoot_chance

        self.setup()

    def setup(self) -> None:
        self.step_timer = self.scene.renderer.ticks
        self.sound = mixer.Sound("assets/sounds/shot_alien.mp3")
        self.sound.set_volume(0.2)
        self.gen_bullet()

    def update(self) -> None:
        self.rect.topleft = (self.x, self.y)
        if random.random() < self.shoot_chance:
            self.shoot()

        now = self.scene.renderer.ticks
        if now - self.step_timer >= self.wait_time:
            self.snake_move()
            self.animate()

            self.step_timer = now

        self.handle_borders()

    def snake_move(self) -> None:
        self.move(self.direction)

        if self.direction[1] == 1:
            self.direction[1] = 0

    def handle_borders(self) -> None:
        game_screen_x: Tuple[int, int] = self.scene.updater.game_screen_x

        sprite_size: Tuple[int, int] = self.sprite.get_size()

        if self.x < game_screen_x[0]:
            self.x = game_screen_x[0]
            self.direction[0] = 1
            self.direction[1] = 1
        elif self.x > game_screen_x[1] - sprite_size[0]:
            self.x = game_screen_x[1] - sprite_size[0]
            self.direction[0] = -1
            self.direction[1] = 1

    def shoot(self) -> None:
        if not self.scene.check_node(self.bullet):
            self.gen_bullet()
            self.scene.nodes.append(self.bullet)
            self.sound.play()

    def gen_bullet(self) -> None:
        sprite_size = self.sprite.get_size()
        self.bullet = AlienProjectile(self.scene, self.x + sprite_size[0] / 2, self.y)
