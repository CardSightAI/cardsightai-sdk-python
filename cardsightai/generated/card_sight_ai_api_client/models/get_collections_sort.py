from enum import Enum


class GetCollectionsSort(str, Enum):
    NAME = "name"

    def __str__(self) -> str:
        return str(self.value)
