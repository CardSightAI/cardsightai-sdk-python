from enum import Enum


class GetRandomReleasesSort(str, Enum):
    NAME = "name"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
