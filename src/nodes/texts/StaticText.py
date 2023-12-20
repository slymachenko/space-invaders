import pygame

# ABSTRACT
from src.abstracts.nodes.Text import Text

# TYPES
from src.abstracts.scenes.Scene import Scene


class StaticText(
    Text,
):
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
        super().__init__(scene, x, y, width, height, text, font_name)
        self.font = pygame.font.SysFont(self.font_name, 30)
        self.surface = self.font.render(self.text, False, (207, 223, 165))

    def update(self) -> None:
        self.surface = self.font.render(self.text, False, (207, 223, 165))

    def render(self) -> None:
        self.scene.renderer.screen.blit(self.surface, (self.x, self.y))
