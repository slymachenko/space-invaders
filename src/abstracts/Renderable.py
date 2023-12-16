from abc import ABC, abstractmethod

from src.core.Renderer import Renderer


class Renderable(ABC):
    renderer: Renderer

    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    @abstractmethod
    def render(self) -> None:
        pass
