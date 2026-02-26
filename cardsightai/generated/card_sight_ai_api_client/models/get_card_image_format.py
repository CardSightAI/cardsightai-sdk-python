from enum import Enum


class GetCardImageFormat(str, Enum):
    JSON = "json"
    RAW = "raw"

    def __str__(self) -> str:
        return str(self.value)
