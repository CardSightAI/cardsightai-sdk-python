from enum import Enum


class GetCollectionBreakdownGroupBy(str, Enum):
    GRADE = "grade"
    MANUFACTURER = "manufacturer"
    PLAYER = "player"
    RELEASE = "release"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
