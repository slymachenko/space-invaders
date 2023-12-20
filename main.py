from src.core.Core import Core
from src.scenes.MainMenuScene import MainMenuScene


def main():
    screen_width: int = 1280
    screen_height: int = 720
    fps: int = 60

    game = Core(MainMenuScene, screen_width, screen_height, fps)
    game.run()


if __name__ == "__main__":
    main()
