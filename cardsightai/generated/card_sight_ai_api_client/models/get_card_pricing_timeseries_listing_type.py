from enum import Enum


class GetCardPricingTimeseriesListingType(str, Enum):
    AUCTION = "auction"
    BOTH = "both"
    FIXED = "fixed"

    def __str__(self) -> str:
        return str(self.value)
