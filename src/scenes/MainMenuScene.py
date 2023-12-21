from src.utils import constants as const

from src.bases.nodes.Sprite import Sprite
from src.nodes.buttons.ChangeSceneButton import (
    ChangeSceneButton,
)
from src.bases.nodes.Text import Text

# BASES
from src.bases.scenes.Scene import Scene

# TYPES
from typing import Tuple
from src.bases.nodes.Node import Node
from src.core.InputManager import InputManager
from src.core.Updater import Updater
from src.core.Renderer import Renderer


class MainMenuScene(Scene):
    nodes: list[Node]

    def __init__(
        self, input_manager: InputManager, updater: Updater, renderer: Renderer
    ):
        self.input_manager = input_manager
        self.updater = updater
        self.renderer = renderer
        self.nodes = list()

        self.setup()

    def setup(self) -> None:
        # load high score
        self.high_score = self.load_high_score()

        # generate background
        self.gen_bg()

        # generate title
        self.gen_title()

        # generate high score
        self.gen_high_score()

        # generate play button
        self.gen_play_btn()

    def load_high_score(self) -> int:
        try:
            with open("high_score.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

    def gen_bg(self) -> None:
        # background sky
        self.nodes.append(
            Sprite(
                self,
                0,
                0,
                self.renderer.screen_width,
                self.renderer.screen_height * 0.6,  # 60% screen height
                "assets/imgs/bg_sky.png",
            )
        )

        bg_sky_sprite_size: Tuple[int, int] = self.nodes[-1].sprite.get_size()

        # background buildings
        self.nodes.append(
            Sprite(
                self,
                0,
                (self.renderer.screen_height * 0.6)
                - bg_sky_sprite_size[1],  # 60% screen height - bg_sky img height
                self.renderer.screen_width,
                1,
                "assets/imgs/bg_buildings.png",
            )
        )

        # background floor
        self.nodes.append(
            Sprite(
                self,
                0,
                self.renderer.screen_height * 0.6,  # 60% screen height
                self.renderer.screen_width,
                self.renderer.screen_height,
                "assets/imgs/bg_floor.png",
            )
        )

    def gen_title(self) -> None:
        # title
        self.nodes.append(
            Sprite(
                self,
                self.renderer.screen_width * 0.5,  # 50% screen width
                self.renderer.screen_height * 0.3,  # 30% screen height
                400,
                200,
                "assets/imgs/title.png",
                rect_mode=const.CENTER,
                wrap_mode=const.CLAMP,
            )
        )

    def gen_high_score(self) -> None:
        # score text
        self.score_text = Text(
            self,
            20,
            20,
            40,
            20,
            f"High Score: {self.high_score}",
            color=const.TEXT_COLOR,
            font_name="assets/fonts/minecraft.ttf",
            font_size=32,
        )

        self.nodes.append(self.score_text)

    def gen_play_btn(self) -> None:
        # play button
        self.nodes.append(
            ChangeSceneButton(
                self,
                self.renderer.screen_width * 0.5,  # 50% screen width
                self.renderer.screen_height * 0.7,  # 70% screen height
                200,
                50,
                "assets/imgs/play_btn.png",
                "PlayScene",
                rect_mode=const.CENTER,
                wrap_mode=const.CLAMP,
            )
        )
