"""Public package interface for barn_owl."""

from .wisdom import owl_wisdom
from .drawing import owl_drawing
from .latin import to_owl_latin
from .jokes import owl_jokes

__all__ = [
    "owl_wisdom",
    "owl_drawing",
    "to_owl_latin",
    "owl_jokes"
]
