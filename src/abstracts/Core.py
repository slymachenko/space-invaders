from abc import ABC, abstractmethod

# TYPES
from src.core.Updater import Updater
from src.core.InputManager import InputManager
from src.core.Renderer import Renderer
from src.abstracts.scenes.Scene import Scene


class Core(ABC):
    screen_width: int
    screen_height: int
    fps: int

    input_manager: InputManager
    updater: Updater
    renderer: Renderer

    current_scene: Scene

    @abstractmethod
    def switch_scene(self, new_scene: Scene) -> None:
        pass

    @abstractmethod
    def run(self) -> None:
        pass
