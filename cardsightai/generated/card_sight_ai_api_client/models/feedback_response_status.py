from enum import Enum


class FeedbackResponseStatus(str, Enum):
    CLOSED = "closed"
    CONFIRMED_BUG = "confirmed_bug"
    DUPLICATE = "duplicate"
    ENHANCEMENT_BACKLOG = "enhancement_backlog"
    ENHANCEMENT_PLANNED = "enhancement_planned"
    FIXED = "fixed"
    NEED_INFO = "need_info"
    NEW = "new"
    NOT_AN_ISSUE = "not_an_issue"
    NOT_REVIEWED = "not_reviewed"
    RELEASED = "released"
    UNDER_REVIEW = "under_review"
    WONT_FIX = "wont_fix"

    def __str__(self) -> str:
        return str(self.value)
