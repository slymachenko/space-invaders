from abc import ABC, abstractmethod


class Renderable(ABC):
    @abstractmethod
    def render(self) -> None:
        pass
