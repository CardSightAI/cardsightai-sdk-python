from enum import Enum


class FeedbackResponseInputStatus(str, Enum):
    DUPLICATE = "duplicate"
    FIXED = "fixed"
    NEED_INFO = "need_info"
    NOT_REVIEWED = "not_reviewed"
    UNDER_REVIEW = "under_review"
    WONT_FIX = "wont_fix"

    def __str__(self) -> str:
        return str(self.value)
