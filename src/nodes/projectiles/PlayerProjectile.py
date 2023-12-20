# CUSTOM MODULES
from src.utils import constants as const

# BASES
from src.bases.nodes.Sprite import Sprite
from src.bases.nodes.Projectile import Projectile

# TYPES
from typing import Tuple
from src.bases.scenes.Scene import Scene


class PlayerProjectile(Projectile, Sprite):
    speed: int

    def __init__(
        self,
        scene: Scene,
        x: int,
        y: int,
        width: int,
        height: int,
        path: str,
        rect_mode: int = const.CLAMP,
        wrap_mode: int = const.CORNER,
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

    def update(self) -> None:
        self.move((0, -1))
        self.rect.topleft = (self.x, self.y)
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
        game_screen_y: Tuple[int, int] = self.scene.updater.game_screen_y
        sprite_size: Tuple[int, int] = self.sprite.get_size()

        if self.y < game_screen_y[0] or self.y > game_screen_y[1] - sprite_size[1]:
            self.scene.remove_node(self)
