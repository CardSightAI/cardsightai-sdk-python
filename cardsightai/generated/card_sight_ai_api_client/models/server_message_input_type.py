from enum import Enum


class ServerMessageInputType(str, Enum):
    INFO = "info"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
