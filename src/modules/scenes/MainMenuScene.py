# CUSTOM MODULES
from src.utils import constants as const
from src.modules.nodes.rects.texture_rects.StaticTextureRect import StaticTextureRect
from src.modules.nodes.rects.texture_rects.buttons.ChangeSceneButton import (
    ChangeSceneButton,
)
from src.modules.scenes.PlayScene import PlayScene

# ABSTRACT
from src.abstracts.scenes.Scene import Scene

# TYPES
from src.abstracts.nodes.Node import Node
from src.core.InputHandler import InputHandler
from src.core.Updater import Updater
from src.core.Renderer import Renderer


class MainMenuScene(Scene):
    nodes: list[Node]

    def __init__(
        self, input_handler: InputHandler, updater: Updater, renderer: Renderer
    ):
        self.input_handler = input_handler
        self.updater = updater
        self.renderer = renderer
        self.nodes = list()

        self.setup()

    def setup(self) -> None:
        # generate background
        self.gen_bg()

        # generate title
        self.gen_title()

        # generate play button
        self.gen_play_btn()

    def gen_bg(self) -> None:
        # background sky
        self.nodes.append(
            StaticTextureRect(
                self,
                0,
                0,
                self.renderer.screen_width,
                self.renderer.screen_height * 0.6,  # 60% screen height
                "assets/bg_sky.png",
            )
        )

        # background buildings
        self.nodes.append(
            StaticTextureRect(
                self,
                0,
                (self.renderer.screen_height * 0.6)
                - self.nodes[-1].img.get_size()[
                    1
                ],  # 60% screen height - bg_sky img height
                self.renderer.screen_width,
                1,
                "assets/bg_buildings.png",
            )
        )

        # background floor
        self.nodes.append(
            StaticTextureRect(
                self,
                0,
                self.renderer.screen_height * 0.6,  # 60% screen height
                self.renderer.screen_width,
                self.renderer.screen_height,
                "assets/bg_floor.png",
            )
        )

    def gen_title(self) -> None:
        # title
        self.nodes.append(
            StaticTextureRect(
                self,
                self.renderer.screen_width * 0.5,  # 50% screen width
                self.renderer.screen_height * 0.3,  # 30% screen height
                400,
                200,
                "assets/title.png",
                rect_mode=const.CENTER,
                wrap_mode=const.CLAMP,
            )
        )

    def gen_play_btn(self) -> None:
        # play button
        self.nodes.append(
            ChangeSceneButton(
                self,
                self.renderer.screen_width * 0.5,  # 50% screen width
                self.renderer.screen_height * 0.7,  # 70% screen height
                200,
                50,
                "assets/play_btn.png",
                "PlayScene",
                rect_mode=const.CENTER,
                wrap_mode=const.CLAMP,
            )
        )

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
