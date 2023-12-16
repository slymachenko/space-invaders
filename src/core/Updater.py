
# TYPES
from src.abstracts.nodes.Node import Node
from src.abstracts.scenes.Scene import Scene

class Updater:
    def __init__(self, game):
        self.game = game

    def update(self, *nodes : list[Node]) -> None:
        for node in nodes:
            node.update()
    
    def switch_scene(self, new_scene: Scene) -> None:
        self.game.switch_scene(new_scene)