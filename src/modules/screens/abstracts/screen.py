from abc import ABC, abstractmethod

# TYPES
from typing import List
from pygame.event import Event
from src.core.renderer import Renderer

class Screen(ABC):
    @abstractmethod
    def input(self, *events : List[Event]) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def render(self, renderer : Renderer) -> None:
        pass
    