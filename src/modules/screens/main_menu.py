import pygame
import math

# CUSTOM MODULES
from src.utils import constants as const

# ABSTRACT
from src.modules.screens.abstracts.screen import Screen

# TYPES
from typing import List, Tuple
from pygame.event import Event
from pygame.surface import Surface
from src.core.renderer import Renderer

class MainMenuScreen(Screen):
    bg_sky_img : Surface
    bg_buildings_img : Surface
    bg_floor_img : Surface
    title_img : Surface

    def __init__(self):
        self.bg_sky_img = pygame.image.load("assets/bg_sky.png")
        self.bg_buildings_img = pygame.image.load("assets/bg_buildings.png")
        self.bg_floor_img = pygame.image.load("assets/bg_floor.png")
        self.title_img = pygame.image.load("assets/title.png")

    def input(self, *events : List[Event]) -> None:
        pass

    def update(self) -> None:
        pass

    def render(self, renderer : Renderer) -> None:
        self.bg_render(renderer)
        self.title_render(renderer)

    def bg_render(self, renderer : Renderer) -> None:
        # SKY
        self.sky_render(renderer)
        
        # BUILDINGS
        self.buidlings_render(renderer)
        
        # FLOOR
        self.floor_render(renderer)

    def sky_render(self, renderer: Renderer) -> None:
        bg_sky_img_size : Tuple(int, int)
        tilesX : int
        tilesY : int

        bg_sky_img_size = self.bg_sky_img.get_size()
        
        tilesX = math.ceil(const.SCREEN_WIDTH / bg_sky_img_size[0])
        tilesY = math.ceil(const.SCREEN_HEIGHT * 0.6 / bg_sky_img_size[1]) # 60% of the screen

        for x in range(tilesX):
            for y in range(tilesY):
                renderer.screen.blit(self.bg_sky_img, (x * bg_sky_img_size[0], y * bg_sky_img_size[1]))

    def buidlings_render(self, renderer : Renderer) -> None:
        bg_buildings_img_size : Tuple(int, int)
        tiles : Tuple(int, int)

        bg_buildings_img_size = self.bg_buildings_img.get_size()

        tiles = (
            math.ceil(const.SCREEN_WIDTH / bg_buildings_img_size[0]),
            math.ceil(const.SCREEN_HEIGHT * 0.6 / bg_buildings_img_size[1]) # 60% of the screen
        )

        for x in range(tiles[0]):
            renderer.screen.blit(self.bg_buildings_img, (x * bg_buildings_img_size[0], (tiles[1] - 1) * bg_buildings_img_size[1]))

    def floor_render(self, renderer : Renderer) -> None:
        img_size : Tuple(int, int)
        tiles : Tuple(int, int)
        tilesY_shift : int

        img_size = self.bg_floor_img.get_size()

        tiles = (
            math.ceil(const.SCREEN_WIDTH / img_size[0]),
            math.ceil(const.SCREEN_HEIGHT * 0.4 / img_size[1]) # 40% of the screen
        )
        tilesY_shift = math.ceil(const.SCREEN_HEIGHT * 0.6 / img_size[1]) # 60% of the screen

        for x in range(tiles[0]):
            for y in range(tiles[1]):
                renderer.screen.blit(self.bg_floor_img, (x * img_size[0], (y + tilesY_shift) * img_size[1]))

    def title_render(self, renderer : Renderer) -> None:
        img_size : Tuple(int, int)
        img_scaled : Surface
        img_scaled_size : Tuple(int, int)
        tiles : Tuple(int, int)

        img_size = self.title_img.get_size()

        # title_img 8x scale
        img_scaled = pygame.transform.scale(self.title_img, (8 * img_size[0], 8 * img_size[1]))

        img_scaled_size = img_scaled.get_size()

        tiles = (
            const.SCREEN_WIDTH * 0.5 - img_scaled_size[0] * 0.5,
            const.SCREEN_HEIGHT * 0.3 - img_scaled_size[1] * 0.5
        )

        renderer.screen.blit(img_scaled, (tiles[0], tiles[1]))