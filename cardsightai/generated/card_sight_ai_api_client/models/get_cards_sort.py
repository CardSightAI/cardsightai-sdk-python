from enum import Enum


class GetCardsSort(str, Enum):
    NAME = "name"
    RELEASE = "release"
    SET = "set"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
