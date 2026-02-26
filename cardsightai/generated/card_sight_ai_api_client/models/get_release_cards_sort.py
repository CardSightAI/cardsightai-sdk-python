from enum import Enum


class GetReleaseCardsSort(str, Enum):
    NAME = "name"
    NUMBER = "number"

    def __str__(self) -> str:
        return str(self.value)
