# BASES
from src.bases.Inputable import Inputable
from src.bases.Updateable import Updateable
from src.bases.Renderable import Renderable

# TYPES
from src.core.InputManager import InputManager
from src.core.Updater import Updater
from src.core.Renderer import Renderer


class Scene(Inputable, Updateable, Renderable):
    input_manager: InputManager
    updater: Updater
    renderer: Renderer

    def __init__(
        self, input_manager: InputManager, updater: Updater, renderer: Renderer
    ):
        self.input_manager = input_manager
        self.updater = updater
        self.renderer = renderer

    def input(self) -> None:
        for node in self.nodes:
            if hasattr(node, "input") and callable(node.input):
                node.input()

    def update(self) -> None:
        for node in self.nodes:
            if hasattr(node, "update") and callable(node.update):
                node.update()

    def render(self) -> None:
        for node in self.nodes:
            if hasattr(node, "render") and callable(node.render):
                node.render()
