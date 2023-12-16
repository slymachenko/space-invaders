from pygame.locals import MOUSEBUTTONDOWN
from pygame import mouse

# CUSTOM MODULES
from src.utils import constants as const
from src.modules.scenes.PlayScene import PlayScene

# ABSTRACTS
from src.modules.nodes.rects.texture_rects.StaticTextureRect import StaticTextureRect
from src.abstracts.nodes.rects.texture_rects.buttons.Button import Button

# TYPES
from src.core.Renderer import Renderer
from src.core.InputHandler import InputHandler
from src.core.Updater import Updater
from pygame.rect import Rect


class PlayButton(StaticTextureRect, Button):
    rect: Rect

    def __init__(
        self,
        renderer: Renderer,
        input_handler: InputHandler,
        updater: Updater,
        x: int,
        y: int,
        width: int,
        height: int,
        path: str,
        rect_mode: int = const.CORNER,
        wrap_mode: int = const.CORNER,
    ):
        super().__init__(renderer, x, y, width, height, path, rect_mode, wrap_mode)
        self.input_handler = input_handler
        self.updater = updater
        self.rect = self.img.get_rect()
        self.rect.topleft = (self.x, self.y)

    def input(self) -> None:
        for event in self.input_handler.events:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = mouse.get_pos()
                if self.rect.collidepoint(mouse_pos):
                    self.updater.switch_scene(
                        PlayScene(self.renderer, self.input_handler, self.updater)
                    )

    def update(self) -> None:
        pass
