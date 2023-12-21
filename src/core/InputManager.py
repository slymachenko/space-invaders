import pygame

from pygame.locals import K_LEFT, K_RIGHT, K_SPACE


class InputManager:
    events: dict["string":int]

    def __init__(self, core):
        self.core = core

    def input(self, *scenes) -> None:
        self.events = {"click": 0, "left": 0, "right": 0, "shoot": 0}

        # Mouse handling
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.core.updater.quit()
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
