from enum import Enum


class PricingRecordListingTypeType0(str, Enum):
    AUCTION = "auction"
    FIXED = "fixed"

    def __str__(self) -> str:
        return str(self.value)
