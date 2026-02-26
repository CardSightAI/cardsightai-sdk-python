from enum import Enum


class GetSegmentsSort(str, Enum):
    NAME = "name"

    def __str__(self) -> str:
        return str(self.value)
