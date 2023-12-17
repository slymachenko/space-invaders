from abc import ABC

from src.abstracts.Renderable import Renderable
from src.abstracts.Inputable import Inputable
from src.abstracts.Updateable import Updateable

# TYPES
from src.core.Renderer import Renderer
from src.core.InputHandler import InputHandler
from src.core.Updater import Updater


class Scene(Inputable, Updateable, Renderable, ABC):
    renderer: Renderer
    updater: Updater
    input_handler: InputHandler

    def __init__(
        self, renderer: Renderer, input_handler: InputHandler, updater: Updater
    ):
        self.renderer = renderer
        self.input_handler = input_handler
        self.updater = updater
