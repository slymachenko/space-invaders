import pygame
import sys

from src.utils import constants as const

class Renderer:
    def __init__(self):
        pygame.init() 
    
        self.screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.is_game_running = True

        # CAPTION
        pygame.display.set_caption("Space Invaders - by slymachenko")

        # ICON
        icon = pygame.image.load('assets/icon.png')
        pygame.display.set_icon(icon)
    
    def input(self) -> None:
        # QUIT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_game_running = False
        
    def update(self, *game_objects) -> None:
        self.clear_screen()
            
        for obj in game_objects:
            obj.update(self)
        
    def render(self, *game_objects) -> None:
        self.clear_screen()
            
        for obj in game_objects:
            obj.render(self)
        
        pygame.display.flip()
        self.clock.tick(const.FPS)

    def clear_screen(self) -> None:
        self.screen.fill((255, 255, 255))
        
    def quit(self) -> None:
        pygame.quit()
        sys.exit(0)