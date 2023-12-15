from src.core.renderer import Renderer

class Game:
    renderer : Renderer

    def __init__(self):
        self.renderer = Renderer()

    def run(self) -> None:
        while self.renderer.is_game_running:
            self.renderer.input()
            
            self.renderer.render()
        
        self.renderer.quit()

if __name__ == "__main__":
    game = Game()
    game.run()