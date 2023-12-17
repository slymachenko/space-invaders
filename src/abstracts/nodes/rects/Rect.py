from src.core.Renderer import Renderer
from src.abstracts.nodes.Node import Node
from src.abstracts.Renderable import Renderable
from abc import ABC

# TYPES
from src.abstracts.scenes.Scene import Scene


class Rect(Node, Renderable, ABC):
    width: int
    height: int

    def __init__(self, scene: Scene, x: int, y: int, width: int, height: int):
        super().__init__(scene, x, y)
        self.width = width
        self.height = height
