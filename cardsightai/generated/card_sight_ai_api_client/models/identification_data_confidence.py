from enum import Enum


class IdentificationDataConfidence(str, Enum):
    HIGH = "High"
    LOW = "Low"
    MEDIUM = "Medium"

    def __str__(self) -> str:
        return str(self.value)
