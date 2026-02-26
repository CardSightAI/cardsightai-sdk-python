from enum import Enum


class GetDetailedHealthResponse200ChecksAdditionalPropertyStatus(str, Enum):
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"

    def __str__(self) -> str:
        return str(self.value)
