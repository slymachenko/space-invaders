from pygame.font import Font

# BASES
from src.bases.nodes.Node import Node
from src.bases.Renderable import Renderable

# TYPES
from typing import Tuple
from src.bases.scenes.Scene import Scene


class Text(Node, Renderable):
    text: str
    color: Tuple[int, int, int]

    font: str

    def __init__(
        self,
        scene: Scene,
        x: int,
        y: int,
        width: int,
        height: int,
        text: str,
        color: Tuple[int, int, int] = (255, 255, 255),
        font_name: str = None,
        font_size: int = 18,
    ):
        super().__init__(scene, x, y, width, height)
        self.text = text
        self.color = color

        self.font = Font(font_name, font_size)

    def render(self):
        self.scene.renderer.screen.blit(
            self.font.render(self.text, True, self.color), (self.x, self.y)
        )
