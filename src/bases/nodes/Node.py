# TYPES
from pygame.rect import Rect
from src.bases.scenes.Scene import Scene


class Node:
    scene: Scene
    x: int
    y: int
    width: int
    height: int

    rect: Rect

    def __init__(self, scene: Scene, x: int, y: int, width: int, height: int):
        self.scene = scene
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.rect = Rect(x, y, width, height)
