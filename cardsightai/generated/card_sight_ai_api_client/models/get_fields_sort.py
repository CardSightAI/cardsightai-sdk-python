from enum import Enum


class GetFieldsSort(str, Enum):
    KEY = "key"
    NAME = "name"
    USAGECOUNT = "usageCount"

    def __str__(self) -> str:
        return str(self.value)
