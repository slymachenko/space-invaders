from abc import ABC
from src.abstracts.scenes.Scene import Scene


class Node(ABC):
    scene: Scene
    x: int
    y: int

    def __init__(self, scene: Scene, x: int, y: int):
        self.scene = scene
        self.x = x
        self.y = y
