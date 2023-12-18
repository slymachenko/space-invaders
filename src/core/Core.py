from src.core.InputHandler import InputHandler
from src.core.Updater import Updater
from src.core.Renderer import Renderer

# ABSTRACTS
from src.abstracts.Core import Core

# TYPES
from src.abstracts.scenes.Scene import Scene


class Core(Core):
    screen_width: int
    screen_height: int
    fps: int

    input_handler: InputHandler
    updater: Updater
    renderer: Renderer

    current_scene: Scene

    def __init__(
        self,
        start_scene: Scene,
        screen_width: int = 1280,
        screen_height: int = 720,
        fps: int = 60,
    ):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.fps = fps

        self.input_handler = InputHandler()
        self.updater = Updater(self)
        self.renderer = Renderer(self.screen_width, self.screen_height, self.fps)

        self.current_scene = start_scene(
            self.input_handler, self.updater, self.renderer
        )

    def switch_scene(self, new_scene: Scene) -> None:
        self.current_scene = new_scene(self.input_handler, self.updater, self.renderer)

    def run(self) -> None:
        while self.input_handler.is_game_running:
            # INPUT HANDLER
            self.input_handler.input((self.current_scene))

            # UPDATER
            self.updater.update((self.current_scene))

            # RENDER
            self.renderer.render((self.current_scene))

        self.input_handler.quit()
