from abc import ABC, abstractmethod

# TYPES
from src.core.Updater import Updater
from src.core.InputHandler import InputHandler
from src.core.Renderer import Renderer
from src.abstracts.scenes.Scene import Scene


class Core(ABC):
    screen_width: int
    screen_height: int
    fps: int

    updater: Updater
    input_handler: InputHandler
    renderer: Renderer

    current_scene: Scene

    @abstractmethod
    def switch_scene(self, new_scene: Scene) -> None:
        pass

    @abstractmethod
    def run(self) -> None:
        pass
