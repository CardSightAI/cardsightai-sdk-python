from enum import Enum


class FeedbackResponseInputEntityType(str, Enum):
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
