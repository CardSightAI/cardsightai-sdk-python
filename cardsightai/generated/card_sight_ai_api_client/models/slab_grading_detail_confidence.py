from enum import Enum


class SlabGradingDetailConfidence(str, Enum):
    HIGH = "High"
    LOW = "Low"
    MEDIUM = "Medium"

    def __str__(self) -> str:
        return str(self.value)
