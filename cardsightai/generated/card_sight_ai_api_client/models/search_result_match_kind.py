from enum import Enum


class SearchResultMatchKind(str, Enum):
    EXACT = "exact"
    FUZZY = "fuzzy"

    def __str__(self) -> str:
        return str(self.value)
