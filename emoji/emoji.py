import random
from typing import List

EMOJIS = {
    "happy": ["😊", "😂", "😄", "😃", "😀", "😁", "😆", "😅", "🤣", "🙂"],
    "sad": ["😢", "😭", "😞", "😔", "😟", "😕", "🙁", "☹️", "😣", "😖"],
    "love": ["❤️", "😍", "😘", "😗", "😙", "😚", "😉", "😘", "💕", "💖"],
    "angry": ["😠", "😡", "😤", "😾", "👿", "💢", "😒", "😏", "😑", "😐"],
}

_VALID_CATEGORIES = set(EMOJIS.keys())


def get_random_emoji(category: str = "happy") -> str:
    """Return a random emoji from the specified category.

    Args:
        category: The category of emojis. Defaults to "happy".

    Returns:
        A random emoji string.

    Raises:
        ValueError: If category is not valid.
    """
    if category not in _VALID_CATEGORIES:
        raise ValueError(f"Unknown category: {category!r}. Choose from: {sorted(_VALID_CATEGORIES)}")
    return random.choice(EMOJIS[category])


def get_emoji(name: str) -> str:
    """Return the emoji for the given name.

    Args:
        name: The name of the emoji.

    Returns:
        The emoji string, or the name if not found.
    """
    # Simple mapping, assume name is like "smile" -> "😊"
    simple_map = {"smile": "😊", "heart": "❤️", "thumbs_up": "👍", "fire": "🔥"}
    return simple_map.get(name, name)


def list_emojis(category: str = None) -> List[str]:
    """List all emojis in a category or all categories.

    Args:
        category: The category to list, or None for all.

    Returns:
        List of emoji strings.
    """
    if category:
        if category not in _VALID_CATEGORIES:
            return []
        return EMOJIS[category]
    else:
        all_emojis = []
        for cat in EMOJIS.values():
            all_emojis.extend(cat)
        return all_emojis


def count_emojis(text: str) -> int:
    """Count the number of emojis in the text.

    Args:
        text: The text to search.

    Returns:
        The count of emojis.
    """
    all_emojis = list_emojis()
    count = 0
    for emoji in all_emojis:
        count += text.count(emoji)
    return count