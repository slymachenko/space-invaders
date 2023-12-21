from src.utils import constants as const
from src.nodes.entities.AlienEntity import AlienEntity
from src.bases.scenes.Scene import Scene

# TYPES
from typing import List, Tuple


class AlienEntityManager:
    scene: Scene
    paths: List[str]
    width: int
    height: int
    offset: Tuple[int, int]

    sprite_size: Tuple[int, int]
    entities: List[AlienEntity]

    def __init__(
        self,
        scene: Scene,
        paths: List[str],
        lines: List[int],
        width: int = 10,
        height: int = 8,
        sprite_size: Tuple[int, int] = (30, 30),
        offset: Tuple[int, int] = (20, 10),
    ):
        self.scene = scene
        self.paths = paths
        self.lines = lines
        self.width = width
        self.height = height
        self.sprite_size = sprite_size
        self.offset = (self.sprite_size[0] + offset[0], self.sprite_size[1] + offset[1])

        self.entities = []

        self.setup()

    def setup(self) -> None:
        self.gen_aliens()

    def gen_aliens(self) -> None:
        screen_shift: Tuple[int, int] = (
            self.scene.renderer.screen_width - self.scene.updater.game_screen_x[1],
            self.scene.renderer.screen_height - self.scene.updater.game_screen_y[1],
        )

        game_screen_width: int = (
            self.scene.updater.game_screen_x[1] - self.scene.updater.game_screen_x[0]
        )
        last_alien_pos_x = (self.width - 1) * self.offset[0]
        aliens_width = last_alien_pos_x + 40
        alien_shift: Tuple[int, int] = (
            (game_screen_width - aliens_width) / 2,
            self.scene.updater.game_screen_y[1] * 0.2,
        )

        shift = 0
        for i, path in enumerate(self.paths):
            self.gen_alien(
                path, screen_shift, alien_shift, (self.width, self.lines[i]), shift
            )

            shift += self.lines[i]

    def gen_alien(
        self,
        path: str,
        screen_shift: Tuple[int, int],
        alien_shift: Tuple[int, int],
        size: Tuple[int, int],
        shift: int = 0,
    ) -> None:
        for i in range(0, size[0]):
            for j in range(shift, size[1] + shift):
                direction: list[int] = [1, 0]
                if j % 2 == 1:
                    direction = [-1, 0]

                self.entities.append(
                    AlienEntity(
                        self.scene,
                        screen_shift[0] + alien_shift[0] + i * self.offset[0],
                        screen_shift[1] + alien_shift[1] + j * self.offset[1],
                        self.sprite_size[0],
                        self.sprite_size[1],
                        path,
                        2,
                        rect_mode=const.CORNER,
                        wrap_mode=const.CLAMP,
                        speed=(10, 40),
                        direction=direction,
                        wait_time=200,
                    )
                )

    def get_aliens(self) -> List[AlienEntity]:
        entities = self.entities
        self.entities = []
        return entities
