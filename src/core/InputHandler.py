import pygame
import sys

from pygame.locals import K_LEFT, K_RIGHT, K_SPACE


class InputHandler:
    is_game_running: bool
    events: dict["string":int]

    def __init__(self):
        self.is_game_running = True

    def input(self, *scenes) -> None:
        self.events = {"click": 0, "left": 0, "right": 0, "shoot": 0}

        # Mouse handling
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.is_game_running = False
                case pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.events["click"] = 1

        # Keyboard handling
        keys: list[int] = pygame.key.get_pressed()

        if keys[K_LEFT]:
            self.events["left"] = 1
        if keys[K_RIGHT]:
            self.events["right"] = 1
        if keys[K_SPACE]:
            self.events["shoot"] = 1

        # Call input for each node
        for scene in scenes:
            scene.input()

    def quit(self) -> None:
        pygame.quit()
        sys.exit(0)
