from enum import Enum


class SearchPricingByTitleListingType(str, Enum):
    AUCTION = "auction"
    BOTH = "both"
    FIXED = "fixed"

    def __str__(self) -> str:
        return str(self.value)
