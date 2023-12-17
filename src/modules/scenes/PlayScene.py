# CUSTOM MODULES
from src.utils import constants as const
from src.modules.nodes.rects.texture_rects.StaticTextureRect import StaticTextureRect
from src.modules.nodes.rects.texture_rects.entities.PlayerEntity import PlayerEntity

# ABSTRACT
from src.abstracts.scenes.Scene import Scene

# TYPES
from src.abstracts.nodes.Node import Node
from src.core.Renderer import Renderer
from src.core.InputHandler import InputHandler
from src.core.Updater import Updater


class PlayScene(Scene):
    nodes: list[Node]

    def __init__(
        self, renderer: Renderer, input_handler: InputHandler, updater: Updater
    ):
        self.renderer = renderer
        self.input_handler = input_handler
        self.updater = updater
        self.nodes = list()

        self.setup()

    def setup(self) -> None:
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

        # player entity
        self.nodes.append(
            PlayerEntity(
                self,
                self.renderer.screen_width * 0.5,  # 50% screen weight
                self.renderer.screen_height * 0.9,  # 60% screen height
                40,
                40,
                "assets/player.png",
                rect_mode=const.CENTER,
                wrap_mode=const.CLAMP,
                speed=10,
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

    def remove_node(self, node: Node) -> None:
        self.nodes.remove(node)

    def check_node(self, node: Node) -> bool:
        if node in self.nodes:
            return True
        return False
