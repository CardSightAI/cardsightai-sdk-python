from enum import Enum


class GetManufacturersSort(str, Enum):
    NAME = "name"

    def __str__(self) -> str:
        return str(self.value)
