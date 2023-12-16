from src.core.Renderer import Renderer
from src.abstracts.nodes.Node import Node
from src.abstracts.Renderable import Renderable
from abc import ABC


class Rect(Node, Renderable, ABC):
    width: int
    height: int

    def __init__(self, renderer: Renderer, x: int, y: int, width: int, height: int):
        super().__init__(renderer, x, y)
        self.width = width
        self.height = height
