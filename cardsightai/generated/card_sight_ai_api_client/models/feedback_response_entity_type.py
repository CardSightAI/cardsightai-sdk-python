from enum import Enum


class FeedbackResponseEntityType(str, Enum):
    CARD = "card"
    GENERAL = "general"
    IDENTIFY = "identify"
    MANUFACTURER = "manufacturer"
    PRODUCT = "product"
    RELEASE = "release"
    SEGMENT = "segment"
    SET = "set"

    def __str__(self) -> str:
        return str(self.value)
