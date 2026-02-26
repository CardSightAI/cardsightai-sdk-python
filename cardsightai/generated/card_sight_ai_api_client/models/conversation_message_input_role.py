from enum import Enum


class ConversationMessageInputRole(str, Enum):
    ASSISTANT = "assistant"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
