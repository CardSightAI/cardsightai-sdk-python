from enum import Enum


class PricingSearchRecordListingTypeType0(str, Enum):
    AUCTION = "auction"
    FIXED = "fixed"

    def __str__(self) -> str:
        return str(self.value)
