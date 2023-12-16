from abc import ABC
from src.core.Renderer import Renderer

class Node(ABC):
    renderer : Renderer
    x : int
    y : int

    def __init__(self, renderer : Renderer, x : int, y : int):
        self.renderer = renderer
        self.x = x
        self.y = y
    