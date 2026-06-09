from enum import Enum


class GetCollectionSetProgressSortBy(str, Enum):
    COMPLETION = "completion"
    DIFFICULTY = "difficulty"
    MISSING = "missing"

    def __str__(self) -> str:
        return str(self.value)
