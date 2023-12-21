from pygame import mouse
from src.utils import constants as const

# BASES
from src.bases.nodes.Button import Button

# TYPES
from src.bases.scenes.Scene import Scene


class ChangeSceneButton(Button):
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
        super().__init__(scene, x, y, width, height, path, rect_mode, wrap_mode)
        self.target_scene = target_scene

    def input(self) -> None:
        if self.scene.input_manager.events["click"]:
            mouse_pos = mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                self.scene.updater.switch_scene(self.target_scene)
