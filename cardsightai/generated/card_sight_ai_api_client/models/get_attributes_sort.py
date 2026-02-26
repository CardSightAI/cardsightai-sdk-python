from enum import Enum


class GetAttributesSort(str, Enum):
    CARDCOUNT = "cardCount"
    NAME = "name"
    SHORTNAME = "shortName"

    def __str__(self) -> str:
        return str(self.value)
