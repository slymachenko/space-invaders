# TYPES
from typing import Tuple
from src.abstracts.nodes.Node import Node
from src.abstracts.scenes.Scene import Scene


class Updater:
    def __init__(self, game):
        self.game = game

        # game screen setup
        screen_width: int = game.renderer.screen_width
        screen_height: int = game.renderer.screen_height

        self.game_screen_x: Tuple[int, int] = (
            (screen_width - screen_height) // 2,
            (screen_width - screen_height) // 2 + screen_height,
        )
        self.game_screen_y: Tuple[int, int] = (
            0,
            screen_height,
        )

    def update(self, *nodes: list[Node]) -> None:
        for node in nodes:
            node.update()

    def switch_scene(self, new_scene: Scene) -> None:
        self.game.switch_scene(new_scene)
