"""UI package initialization."""

from .components import UIComponents
from .templates import CSS_STYLES, BOT_MESSAGE_TEMPLATE, USER_MESSAGE_TEMPLATE

__all__ = [
    "UIComponents",
    "CSS_STYLES",
    "BOT_MESSAGE_TEMPLATE",
    "USER_MESSAGE_TEMPLATE",
]
