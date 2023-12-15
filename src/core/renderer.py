import pygame
import sys

from src.utils import constants

class Renderer:
    def __init__(self):
        pygame.init() 
    
        self.screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.is_game_running = True

        # CAPTION
        pygame.display.set_caption("Space Invaders - by slymachenko")

        # ICON
        icon = pygame.image.load('assets/icon.png')
        pygame.display.set_icon(icon)
    
    def render(self) -> None:
        self.screen.fill((255, 255, 255))
        
        pygame.display.flip()
        self.clock.tick(constants.FPS)

    def input(self) -> None:
        # QUIT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_game_running = False

    def quit(self) -> None:
        pygame.quit()
        sys.exit(0)