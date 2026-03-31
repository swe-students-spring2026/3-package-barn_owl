"""
Contains all functions related to owl jokes.
"""

import random
from typing import Dict, List

_JOKES: Dict[str, List[str]] = {
    "python": [
        "Why did the Python programmer break up usually They needed more space!",
        "What do you call a Python developer who loves coffee? A brew-tiful coder!",
        "Why was the Python data scientist bad at relationships? They kept getting lost in their data frames!",
        "How does a Python programmer party? They throw exceptions!",
        "Why did the Python programmer get kicked out of class? They kept raising their hand!",
    ],
    "programming": [
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "What do you call a programmer from Finland? Nerdic.",
        "Why did the computer go to the doctor? It had a virus!",
        "How do you comfort a JavaScript bug? You console it.",
        "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
    ],
    "cold": [
        "What is a Barn Owl’s favourite subject at school? Owlgebra!",
        "What do you call an owl in winter? A snowl.",
        "What do you call fake spaghetti? An impasta!",
        "What’s an owl’s favourite band? The WHO!",
        "What do you call a bear with no teeth? A gummy bear!",
        "What do you call an owl with a low voice? A growl!"
    ],
}

_VALID_CATEGORIES = set(_JOKES.keys())

def owl_jokes(category: str = "python") -> str:
    """
    Return a random owl-themed joke.

    Args:
        category: The joke category. One of ``"python"``, ``"programming"``,
            or ``"cold"``. Defaults to ``"python"``.

    Returns:
        A string containing one owl joke.

    Raises:
        ValueError: If *category* is not recognised.
    """
    if category not in _VALID_CATEGORIES:
        raise ValueError(
            f"Unknown category: {category!r}. "
            f"Choose from: {sorted(_VALID_CATEGORIES)}"
        )
    return random.choice(_JOKES[category])