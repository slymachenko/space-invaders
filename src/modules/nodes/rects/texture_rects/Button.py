import pygame
# CUSTOM MODULES
from src.utils import constants as const

from src.modules.nodes.rects.texture_rects.StaticTextureRect import StaticTextureRect
from src.abstracts.Inputable import Inputable
from src.abstracts.Updateable import Updateable

# TYPES
from src.core.Renderer import Renderer
from src.core.InputHandler import InputHandler
from src.core.Updater import Updater
from pygame.rect import Rect


class Button(StaticTextureRect, Inputable, Updateable):
    rect : Rect

    def __init__(self, renderer : Renderer, input_handler : InputHandler, updater: Updater, x : int, y : int, width : int, height : int, path : str, rect_mode : int = const.CORNER, wrap_mode : int = const.CORNER):
        super().__init__(renderer, x, y, width, height, path, rect_mode, wrap_mode)
        self.input_handler = input_handler
        self.rect = self.img.get_rect()
        self.rect.topleft = (self.x, self.y)

    def input(self):
        for event in self.input_handler.events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if self.rect.collidepoint(mouse_pos):
                    print("CLIKED")

    def update(self):
        pass