import pygame
import sys

# TYPES
from pygame.event import Event

class InputHandler:
    is_game_running : bool
    events : list[Event]

    def __init__(self):
        self.is_game_running = True
    
    def input(self, *nodes) -> None:
        self.events = list()
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.is_game_running = False
                case _:
                    self.events.append(event)

        for node in nodes:
            node.input()
        
    def quit(self) -> None:
        pygame.quit()
        sys.exit(0)