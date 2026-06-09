from enum import Enum


class GetCardMarketplaceListingType(str, Enum):
    AUCTION = "auction"
    BOTH = "both"
    FIXED = "fixed"

    def __str__(self) -> str:
        return str(self.value)
