from enum import Enum


class GetRandomCardsSort(str, Enum):
    NAME = "name"
    RELEASE = "release"
    SET = "set"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
