from enum import Enum


class GetCollectionCardsSort(str, Enum):
    BUYDATE = "buyDate"
    BUYPRICE = "buyPrice"
    SOLDDATE = "soldDate"
    SOLDPRICE = "soldPrice"

    def __str__(self) -> str:
        return str(self.value)
