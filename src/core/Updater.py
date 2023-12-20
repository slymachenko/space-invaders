# TYPES
from typing import Tuple

# from src.modules.scenes.PlayScene import PlayScene
# from src.modules.scenes.MainMenuScene import MainMenuScene


class Updater:
    is_game_running: bool

    def __init__(self, core):
        self.is_game_running = True
        self.core = core

        # game screen setup
        screen_width: int = core.screen_width
        screen_height: int = core.screen_height

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

    def switch_scene(self, scene_name) -> None:
        match scene_name:
            case "PlayScene":
                from src.scenes.PlayScene import PlayScene

                self.core.switch_scene(PlayScene)
            case "MainMenuScene":
                from src.scenes.MainMenuScene import MainMenuScene

                self.core.switch_scene(MainMenuScene)

    def quit(self) -> None:
        self.is_game_running = False
