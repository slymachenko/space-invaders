# TYPES
from typing import Tuple


class Updater:
    def __init__(self, game):
        self.game = game

        # game screen setup
        screen_width: int = game.screen_width
        screen_height: int = game.screen_height

        self.game_screen_x: Tuple[int, int] = (
            (screen_width - screen_height) // 2,
            (screen_width - screen_height) // 2 + screen_height,
        )
        self.game_screen_y: Tuple[int, int] = (
            0,
            screen_height,
        )

    def update(self, *scenes) -> None:
        for scene in scenes:
            scene.update()

    def switch_scene(self, new_scene) -> None:
        self.game.switch_scene(new_scene)
