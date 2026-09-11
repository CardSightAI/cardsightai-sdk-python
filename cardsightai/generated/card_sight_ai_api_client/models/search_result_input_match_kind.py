from enum import Enum


class SearchResultInputMatchKind(str, Enum):
    EXACT = "exact"
    FUZZY = "fuzzy"

    def __str__(self) -> str:
        return str(self.value)
