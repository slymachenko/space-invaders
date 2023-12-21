from src.utils import constants as const
from src.bases.nodes.Sprite import Sprite
from src.bases.nodes.Text import Text
from src.nodes.entities.PlayerEntity import PlayerEntity

from src.nodes.entities.AlienEntity import AlienEntity
from src.nodes.entities.AlienEntityManager import AlienEntityManager
from src.nodes.projectiles.PlayerProjectile import (
    PlayerProjectile,
)
from src.nodes.projectiles.AlienProjectile import (
    AlienProjectile,
)

# BASES
from src.bases.scenes.Scene import Scene

# TYPES
from typing import Tuple
from src.bases.nodes.Node import Node
from src.core.Renderer import Renderer
from src.core.InputManager import InputManager
from src.core.Updater import Updater


class PlayScene(Scene):
    nodes: list[Node]
    score: int
    alien_manager: AlienEntityManager

    def __init__(
        self, input_manager: InputManager, updater: Updater, renderer: Renderer
    ):
        self.input_manager = input_manager
        self.updater = updater
        self.renderer = renderer

        self.nodes = list()
        self.score = 0
        alien_paths = [
            "assets/imgs/alien4.png",
            "assets/imgs/alien3.png",
            "assets/imgs/alien2.png",
            "assets/imgs/alien1.png",
        ]
        alien_lines = [1, 1, 2, 2]
        alien_shoot_chances = [0.001, 0.001, 0, 0]
        self.alien_manager = AlienEntityManager(
            self, alien_paths, alien_lines, alien_shoot_chances
        )

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
            Sprite(
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
            Sprite(
                self,
                0,
                (self.renderer.screen_height * 0.6)
                - self.nodes[-1].sprite.get_size()[
                    1
                ],  # 60% screen height - bg_sky img height
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

    def gen_score(self) -> None:
        # score text
        self.score_text = Text(
            self,
            20,
            20,
            40,
            20,
            f"Score: {self.score}",
            color=const.TEXT_COLOR,
            font_name="assets/fonts/minecraft.ttf",
            font_size=32,
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
        self.nodes += self.alien_manager.get_aliens()

    def remove_node(self, node: Node) -> None:
        self.nodes.remove(node)

    def check_node(self, node: Node) -> bool:
        if node in self.nodes:
            return True
        return False

    def update_score_text(self) -> None:
        self.score_text.text = f"Score: {self.score}"

    def update(self) -> None:
        super().update()

        are_aliens: bool = False

        for node in self.nodes:
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
                        self.end_game()

                are_aliens = True

            if isinstance(node, PlayerEntity):
                for other_node in self.nodes:
                    if isinstance(
                        other_node, AlienProjectile
                    ) and other_node.rect.colliderect(node.rect):
                        self.end_game()

        if not are_aliens:
            if self.alien_manager.wait_time > 100:
                self.alien_manager.wait_time *= 0.75
            else:
                self.alien_manager.wait_time = 100
            self.alien_manager.gen_aliens()
            self.nodes += self.alien_manager.get_aliens()

    def end_game(self) -> None:
        self.save_score()
        self.updater.switch_scene("MainMenuScene")

    def save_score(self) -> None:
        with open("high_score.txt", "w") as file:
            file.write(str(self.score))
