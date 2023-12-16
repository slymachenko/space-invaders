from src.core.Updater import Updater
from src.core.Renderer import Renderer
from src.core.InputHandler import InputHandler

from src.modules.scenes.MainMenuScene import MainMenuScene

# TYPES
from src.abstracts.scenes.Scene import Scene

screen_width = 1280
screen_height = 720
fps = 60

class Game:
    renderer : Renderer
    input_handler : InputHandler
    current_scene : Scene 

    def __init__(self):
        self.renderer = Renderer(screen_width, screen_height, fps)
        self.input_handler = InputHandler()
        self.updater = Updater()
        self.current_scene = MainMenuScene(self.renderer, self.input_handler, self.updater)

    def switch_scene(self, new_scene : Scene) -> None:
        self.current_scene = new_scene

    def run(self) -> None:
        while self.input_handler.is_game_running:
            # INPUT HANDLER
            self.input_handler.input((self.current_scene))

            # UPDATER
            self.updater.update((self.current_scene))

            # RENDER
            self.renderer.render((self.current_scene))
        
        self.input_handler.quit()

if __name__ == "__main__":
    game = Game()
    game.run()