from enum import Enum


class FeedbackResponseInputFeedbackTypeType0(str, Enum):
    BUG = "bug"
    DATA_ERROR = "data_error"
    MISSING_DATA = "missing_data"
    OTHER = "other"
    SUGGESTION = "suggestion"

    def __str__(self) -> str:
        return str(self.value)
