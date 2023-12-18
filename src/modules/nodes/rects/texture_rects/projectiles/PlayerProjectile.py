# CUSTOM MODULES
from src.utils import constants as const

# ABSTRACTS
from src.modules.nodes.rects.texture_rects.StaticTextureRect import StaticTextureRect
from src.abstracts.nodes.rects.texture_rects.projectiles.Projectile import Projectile

# TYPES
from typing import Tuple
from src.abstracts.scenes.Scene import Scene


class PlayerProjectile(Projectile, StaticTextureRect):
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
        img_size: Tuple[int, int] = self.img.get_size()

        if self.y < game_screen_y[0] or self.y > game_screen_y[1] - img_size[1]:
            self.scene.remove_node(self)
