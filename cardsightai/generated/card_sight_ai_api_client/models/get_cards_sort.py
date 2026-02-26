from enum import Enum


class GetCardsSort(str, Enum):
    NAME = "name"
    PRICE_RAW = "price-raw"
    RELEASE = "release"
    SET = "set"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
