from enum import Enum


class SlabGradingDetailInputConfidence(str, Enum):
    HIGH = "High"
    LOW = "Low"
    MEDIUM = "Medium"

    def __str__(self) -> str:
        return str(self.value)
