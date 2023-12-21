from abc import ABC, abstractmethod


class Inputable(ABC):
    @abstractmethod
    def input(self) -> None:
        pass
