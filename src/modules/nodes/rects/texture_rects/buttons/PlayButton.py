from pygame.locals import MOUSEBUTTONDOWN
from pygame import mouse

# CUSTOM MODULES
from src.utils import constants as const
from src.modules.scenes.PlayScene import PlayScene

# ABSTRACTS
from src.modules.nodes.rects.texture_rects.StaticTextureRect import StaticTextureRect
from src.abstracts.nodes.rects.texture_rects.buttons.Button import Button

# TYPES
from src.abstracts.scenes.Scene import Scene


class PlayButton(StaticTextureRect, Button):
    def __init__(
        self,
        scene: Scene,
        x: int,
        y: int,
        width: int,
        height: int,
        path: str,
        rect_mode: int = const.CORNER,
        wrap_mode: int = const.CLAMP,
    ):
        super().__init__(scene, x, y, width, height, path, rect_mode, wrap_mode)

    def input(self) -> None:
        if self.scene.input_handler.events["click"]:
            mouse_pos = mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                self.scene.updater.switch_scene(
                    PlayScene(
                        self.scene.renderer,
                        self.scene.input_handler,
                        self.scene.updater,
                    )
                )

    def update(self) -> None:
        pass
