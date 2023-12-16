import pygame

# CUSTOM MODULES
from src.utils import constants as const

# TYPES
from pygame.time import Clock
from pygame.surface import Surface

class Renderer:
    screen_width : int
    screen_height : int
    fps : int
    screen : Surface
    clock : Clock

    def __init__(self, screen_width : int, screen_height : int, fps : int):
        self.screen_width = screen_width if screen_width > const.SCREEN_WIDTH_MIN else const.SCREEN_WIDTH_MIN
        self.screen_height = screen_height if screen_height > const.SCREEN_HEIGHT_MIN else const.SCREEN_HEIGHT_MIN
        self.fps = fps

        self.setup()
        
    def setup(self) -> None:
        pygame.init() 
    
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = Clock()

        # CAPTION
        pygame.display.set_caption("Space Invaders - by slymachenko")

        # ICON
        icon = pygame.image.load('assets/icon.png')
        pygame.display.set_icon(icon)
        
    def render(self, *nodes) -> None:
        self.clear_screen()
            
        for node in nodes:
            if hasattr(node, 'render') and callable(node.render):
                node.render()
        
        pygame.display.flip()
        self.clock.tick(self.fps)

    def clear_screen(self) -> None:
        self.screen.fill((255, 255, 255))