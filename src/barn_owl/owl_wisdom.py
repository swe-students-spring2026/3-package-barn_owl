import random

_WISDOM: dict[str, list[str]] = {
    "life": [
        "The owl who flies at night sees what the eagle misses by day.",
        "Silence is not empty; it is full of answers — hoo hoo.",
        "Turn your head 270 degrees before you judge a situation.",
        "Even in darkness, keep your eyes wide open.",
        "A wise owl knows when to speak and, more importantly, when to hoot softly.",
        "Sleep is not laziness; it is the preparation of a nocturnal mind.",
        "The tallest tree in the forest once started as a tiny perch for a small owl.",
    ],
    "coding": [
        "A function that does one thing does that one thing well — hoo hoo.",
        "Refactor like a barn owl: silently, swiftly, and without disturbing the prey.",
        "The best code is the code you don't have to write.",
        "An owl never deploys to production on a Friday night... unless the prey demands it.",
        "Read the error message. Hoo hoo. Read it again.",
        "Comments are the parliament of thoughts — use them wisely and sparingly.",
        "The wise developer tests their code before the code tests their patience.",
        "Debugging is just hunting by another name. Be patient; the bug will reveal itself.",
    ],
    "friendship": [
        "A true friend is one who sits quietly beside you in the dark — hoo hoo.",
        "Choose your parliament wisely; owls are known by the company they roost with.",
        "Even a lone owl appreciates a friendly hoot across the forest.",
        "The best friendships, like the best branches, hold firm in any storm.",
        "Share your pellets; you never know when the night will grow long.",
        "A friend who listens is worth more than one who speaks.",
    ],
    "nature": [
        "The forest remembers every owl that has ever perched in its branches.",
        "Rain does not apologize to the owl — and the owl does not apologize to the rain.",
        "The moon is not a lamp; it is a map for those wise enough to read it.",
        "A tree fallen in the forest still makes an excellent perch — hoo hoo.",
        "Every night sky holds more stars than there are reasons to worry.",
        "The wind does not hurry, yet it travels everywhere.",
    ],
    "food": [
        "Do not chase every mouse; choose your prey with intention.",
        "The vole that runs in daylight becomes supper by moonrise.",
        "A full belly makes for a wise owl; an empty belly makes for a desperate one.",
        "Swallow life whole, then sort out what you truly needed — hoo hoo.",
        "The patient owl eats; the impatient owl goes hungry.",
        "Never regurgitate more pellets than you can use in one sitting.",
    ],
}

_VALID_TOPICS = set(_WISDOM.keys())


def owl_wisdom(topic: str = "life") -> str:
    """Return a random owl-themed proverb or fortune.

    Args:
        topic: The theme of the wisdom. One of ``"life"``, ``"coding"``,
            ``"friendship"``, ``"nature"``, or ``"food"``.
            Defaults to ``"life"``.

    Returns:
        A string containing one owl wisdom quote.

    Raises:
        ValueError: If *topic* is not recognised.
    """
    if topic not in _VALID_TOPICS:
        raise ValueError(
            f"Unknown topic: {topic!r}. "
            f"Choose from: {sorted(_VALID_TOPICS)}"
        )
    return random.choice(_WISDOM[topic])
