from enum import Enum


class MarketplaceSearchRecordListingTypeType0(str, Enum):
    AUCTION = "auction"
    FIXED = "fixed"
    SEARCH = "search"

    def __str__(self) -> str:
        return str(self.value)
