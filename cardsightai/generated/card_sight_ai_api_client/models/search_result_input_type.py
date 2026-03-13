from enum import Enum


class SearchResultInputType(str, Enum):
    CARD = "card"
    PARALLEL = "parallel"
    RELEASE = "release"
    SET = "set"

    def __str__(self) -> str:
        return str(self.value)
