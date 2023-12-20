# CUSTOM MODULES
from src.utils import constants as const
from src.modules.nodes.rects.texture_rects.StaticTextureRect import StaticTextureRect
from src.modules.nodes.rects.texts.StaticText import StaticText
from src.modules.nodes.rects.texture_rects.entities.PlayerEntity import PlayerEntity
from src.modules.nodes.rects.texture_rects.entities.AlienEntity import AlienEntity
from src.modules.nodes.rects.texture_rects.projectiles.PlayerProjectile import (
    PlayerProjectile,
)

# ABSTRACT
from src.abstracts.scenes.Scene import Scene

# TYPES
from typing import Tuple
from src.abstracts.nodes.Node import Node
from src.core.Renderer import Renderer
from src.core.InputHandler import InputHandler
from src.core.Updater import Updater


class PlayScene(Scene):
    nodes: list[Node]
    score: int

    def __init__(
        self, input_handler: InputHandler, updater: Updater, renderer: Renderer
    ):
        self.input_handler = input_handler
        self.updater = updater
        self.renderer = renderer

        self.nodes = list()
        self.score = 0

        self.setup()

    def setup(self) -> None:
        # generate background
        self.gen_bg()

        # generate score
        self.gen_score()

        # generate player entity
        self.gen_player()

        # generate aliens
        self.gen_aliens()

    def gen_bg(self) -> None:
        # background sky
        self.nodes.append(
            StaticTextureRect(
                self,
                0,
                0,
                self.renderer.screen_width,
                self.renderer.screen_height * 0.6,  # 60% screen height
                "assets/imgs/bg_sky.png",
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
                "assets/imgs/bg_buildings.png",
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
                "assets/imgs/bg_floor.png",
            )
        )

    def gen_score(self) -> None:
        # score text
        self.score_text = StaticText(
            self, 20, 20, 40, 20, f"Score: {self.score}", "Comic Sans MS"
        )

        self.nodes.append(self.score_text)

    def gen_player(self) -> None:
        # player entity
        self.nodes.append(
            PlayerEntity(
                self,
                self.renderer.screen_width * 0.5,  # 50% screen weight
                self.renderer.screen_height * 0.8,  # 60% screen height
                40,
                40,
                "assets/imgs/player.png",
                rect_mode=const.CENTER,
                wrap_mode=const.CLAMP,
                speed=(10, 10),
            )
        )

    def gen_aliens(self) -> None:
        columns: int = 10

        offset: Tuple[int, int] = (60, 40)

        screen_shift: Tuple[int, int] = (
            self.renderer.screen_width - self.updater.game_screen_x[1],
            self.renderer.screen_height - self.updater.game_screen_y[1],
        )

        game_screen_width: int = (
            self.updater.game_screen_x[1] - self.updater.game_screen_x[0]
        )
        last_alien_pos_x = (columns - 1) * offset[0]
        aliens_width = last_alien_pos_x + 40
        alien_shift: Tuple[int, int] = (
            (game_screen_width - aliens_width) / 2,
            self.updater.game_screen_y[1] * 0.2,
        )

        self.gen_alien(
            "assets/imgs/alien4.png",
            screen_shift,
            alien_shift,
            offset,
            (columns, 1),
        )

        self.gen_alien(
            "assets/imgs/alien3.png",
            screen_shift,
            alien_shift,
            offset,
            (columns, 1),
            shift=1,
        )

        self.gen_alien(
            "assets/imgs/alien2.png",
            screen_shift,
            alien_shift,
            offset,
            (columns, 2),
            shift=2,
        )

        self.gen_alien(
            "assets/imgs/alien1.png",
            screen_shift,
            alien_shift,
            offset,
            (columns, 2),
            shift=4,
        )

    def gen_alien(
        self,
        path: str,
        screen_shift: Tuple[int, int],
        alien_shift: Tuple[int, int],
        offset: Tuple[int, int],
        size: Tuple[int, int],
        shift: int = 0,
    ) -> None:
        for i in range(0, size[0]):
            for j in range(shift, size[1] + shift):
                direction: list[int] = [1, 0]
                if j % 2 == 1:
                    direction = [-1, 0]

                self.nodes.append(
                    AlienEntity(
                        self,
                        screen_shift[0] + alien_shift[0] + i * offset[0],
                        screen_shift[1] + alien_shift[1] + j * offset[1],
                        30,
                        30,
                        path,
                        rect_mode=const.CORNER,
                        wrap_mode=const.CLAMP,
                        speed=(10, 40),
                        direction=direction,
                        wait_time=300,
                    )
                )

    def remove_node(self, node: Node) -> None:
        self.nodes.remove(node)

    def check_node(self, node: Node) -> bool:
        if node in self.nodes:
            return True
        return False

    def update_score_text(self) -> None:
        self.score_text.text = f"Score: {self.score}"

    def input(self) -> None:
        for node in self.nodes:
            if hasattr(node, "input") and callable(node.input):
                node.input()

    def update(self) -> None:
        are_aliens: bool = False

        for node in self.nodes:
            if hasattr(node, "update") and callable(node.update):
                node.update()

            if isinstance(node, AlienEntity):
                for other_node in self.nodes:
                    if isinstance(
                        other_node, PlayerProjectile
                    ) and other_node.rect.colliderect(node.rect):
                        self.remove_node(other_node)
                        self.remove_node(node)
                        self.score += 10
                        self.update_score_text()

                    if isinstance(
                        other_node, PlayerEntity
                    ) and other_node.rect.colliderect(node.rect):
                        self.save_score()
                        self.updater.switch_scene("MainMenuScene")

                are_aliens = True

        if not are_aliens:
            self.gen_aliens()

    def render(self) -> None:
        for node in self.nodes:
            if hasattr(node, "render") and callable(node.render):
                node.render()

    def save_score(self) -> None:
        with open("high_score.txt", "w") as file:
            file.write(str(self.score))
