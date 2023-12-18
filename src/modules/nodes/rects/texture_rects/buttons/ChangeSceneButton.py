from pygame import mouse

# CUSTOM MODULES
from src.utils import constants as const

# ABSTRACTS
from src.modules.nodes.rects.texture_rects.StaticTextureRect import StaticTextureRect
from src.abstracts.nodes.rects.texture_rects.buttons.Button import Button

# TYPES
from src.abstracts.scenes.Scene import Scene


class ChangeSceneButton(Button, StaticTextureRect):
    def __init__(
        self,
        scene: Scene,
        x: int,
        y: int,
        width: int,
        height: int,
        path: str,
        target_scene: Scene,
        rect_mode: int = const.CORNER,
        wrap_mode: int = const.CLAMP,
    ):
        super().__init__(
            scene, x, y, width, height, path, target_scene, rect_mode, wrap_mode
        )

    def input(self) -> None:
        if self.scene.input_handler.events["click"]:
            mouse_pos = mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                self.scene.updater.switch_scene(self.target_scene)

    def update(self) -> None:
        pass
