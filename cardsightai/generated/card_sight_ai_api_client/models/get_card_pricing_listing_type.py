from enum import Enum


class GetCardPricingListingType(str, Enum):
    AUCTION = "auction"
    BOTH = "both"
    FIXED = "fixed"

    def __str__(self) -> str:
        return str(self.value)
