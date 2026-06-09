from enum import Enum


class ServerMessageType(str, Enum):
    INFO = "info"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
