from enum import Enum


class GetSetCardsSort(str, Enum):
    NAME = "name"
    NUMBER = "number"

    def __str__(self) -> str:
        return str(self.value)
