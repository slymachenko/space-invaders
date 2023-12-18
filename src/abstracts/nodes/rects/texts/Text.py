from abc import ABC

# ABSTRACT
from src.abstracts.nodes.rects.Rect import Rect

# TYPES
from src.abstracts.scenes.Scene import Scene


class Text(Rect, ABC):
    text: str
    font_name: str

    def __init__(
        self,
        scene: Scene,
        x: int,
        y: int,
        width: int,
        height: int,
        text: str,
        font_name: str,
    ):
        super().__init__(scene, x, y, width, height)
        self.text = text
        self.font_name = font_name
