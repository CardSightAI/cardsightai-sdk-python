from enum import Enum


class GetCollectionBreakdownSortBy(str, Enum):
    COUNT = "count"
    PERCENTAGE = "percentage"
    ROI = "roi"
    VALUE = "value"

    def __str__(self) -> str:
        return str(self.value)
