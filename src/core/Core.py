from pygame import quit

from pygame.image import load
from pygame.display import set_caption
from pygame.display import set_icon

from src.core.InputManager import InputManager
from src.core.Updater import Updater
from src.core.Renderer import Renderer

# TYPES
from src.bases.scenes.Scene import Scene


class Core:
    screen_width: int
    screen_height: int
    fps: int

    input_manager: InputManager
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

        self.input_manager = InputManager(self)
        self.updater = Updater(self)
        self.renderer = Renderer(self.screen_width, self.screen_height, self.fps)

        self.current_scene = start_scene(
            self.input_manager, self.updater, self.renderer
        )

        self.setup()

    def setup(self) -> None:
        # CAPTION
        set_caption("Space Invaders - by slymachenko")

        # ICON
        icon = load("assets/imgs/icon.png")
        set_icon(icon)

    def switch_scene(self, new_scene: Scene) -> None:
        self.current_scene = new_scene(self.input_manager, self.updater, self.renderer)

    def run(self) -> None:
        while self.updater.is_game_running:
            # INPUT HANDLER
            self.input_manager.input((self.current_scene))

            # UPDATER
            self.updater.update((self.current_scene))

            # RENDER
            self.renderer.render((self.current_scene))

        quit()
