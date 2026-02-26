from enum import Enum


class GetReleasesSort(str, Enum):
    NAME = "name"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
