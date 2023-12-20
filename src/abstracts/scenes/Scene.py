from abc import ABC

# ABSTRACTS
from src.abstracts.Inputable import Inputable
from src.abstracts.Updateable import Updateable
from src.abstracts.Renderable import Renderable

# TYPES
from src.core.InputManager import InputManager
from src.core.Updater import Updater
from src.core.Renderer import Renderer


class Scene(Inputable, Updateable, Renderable, ABC):
    input_manager: InputManager
    updater: Updater
    renderer: Renderer

    def __init__(
        self, input_manager: InputManager, updater: Updater, renderer: Renderer
    ):
        self.input_manager = input_manager
        self.updater = updater
        self.renderer = renderer
