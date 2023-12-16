from src.core.renderer import Renderer

from src.modules.screens.main_menu import MainMenuScreen

# TYPES
from src.modules.screens.abstracts.screen import Screen

class Game:
    renderer : Renderer
    current_screen : Screen 

    def __init__(self):
        self.renderer = Renderer()
        self.current_screen = MainMenuScreen()

    def switch_screen(self, new_screen : Screen) -> None:
        self.current_screen = new_screen

    def run(self) -> None:
        while self.renderer.is_game_running:
            # INPUT HANDLER
            self.renderer.input()

            # RENDER
            self.renderer.render((self.current_screen))
        
        self.renderer.quit()

if __name__ == "__main__":
    game = Game()
    game.run()