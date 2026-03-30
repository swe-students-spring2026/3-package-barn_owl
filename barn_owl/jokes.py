"""
Contains all functions related to owl jokes.
"""

import random

_JOKES: dict[str, list[str]] = {
    "python": [
        "Why did the Python programmer break up with their partner? They needed more space!",
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
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "What do you call a bear with no teeth? A gummy bear!",
        "Why can't you give Elsa a balloon? Because she will let it go.",
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