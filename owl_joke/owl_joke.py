import random
from typing import List

JOKES = {
    "wise": [
        "Why did the owl become a philosopher? Because it was wise to the ways of the night!",
        "What do you call an owl who tells jokes? A hoot comedian!",
        "Why was the owl a great detective? It always had its eyes on the prize!",
        "How does an owl end a letter? 'Owl be seeing you!'",
        "Why did the owl join the library? It wanted to be surrounded by wise cracks!",
        "What did the owl say to its Valentine? 'Owl always love you!'",
        "Why don't owls play hide and seek? Because good luck hiding when you're always watching!",
        "How do owls stay cool in summer? They use their fans... their wings!",
        "Why was the owl promoted? It was outstanding in its field!",
        "What do you call an owl magician? Hoo-dini!",
    ],
    "funny": [
        "Why did the owl bring a ladder to school? It heard the class was going to new heights!",
        "What do you call an owl with a sore throat? A bird that doesn't give a hoot!",
        "Why did the owl go to the doctor? It was feeling a bit 'fowl'!",
        "How do owls send secret messages? By using their 'owl-code'!",
        "Why did the owl refuse to share its food? It was too 'owl-fish'!",
        "What did the owl say when it was surprised? 'Owl my goodness!'",
        "Why did the owl wear a raincoat? Because it heard it was going to be a hoot outside!",
        "How do owls apologize? They say 'I'm sorry if I ruffled your feathers!'",
        "Why did the owl become a banker? It was great at handling 'owl' the money!",
        "What do you call an owl who loves to dance? A boogie-owl!",
    ],
    "programming": [
        "Why did the owl learn Python? Because it wanted to be a 'wise' coder!",
        "What do you call an owl debugging code? A 'hoot'-spot finder!",
        "Why did the owl join GitHub? It wanted to branch out!",
        "How does an owl fix a bug? It 'owls' over the code carefully!",
        "Why did the owl become a developer? It loved working in the 'night' shift!",
        "What do you call an owl writing JavaScript? A 'hoot'-script programmer!",
        "Why did the owl avoid using tabs? It preferred 'spaces' for nesting!",
        "How do owls handle exceptions? They 'catch' them with their talons!",
        "Why did the owl love recursion? It could go 'owl' night long!",
        "What do you call an owl testing code? A 'wise' QA tester!",
    ],
    "nature": [
        "Why did the owl love the forest? It was a 'hoot' to live there!",
        "What do you call an owl in the rain? A wet 'hoot'!",
        "Why did the owl climb the tree? It wanted a better 'view'!",
        "How do owls enjoy the moonlight? They have 'owl'-moon parties!",
        "Why did the owl avoid the city? Too much 'noise' pollution!",
        "What do you call an owl watching stars? A 'wise' astronomer!",
        "Why did the owl love autumn? All the falling leaves made great camouflage!",
        "How do owls survive winter? They 'owl'-ways stay warm!",
        "Why did the owl visit the lake? It heard the fish were 'fin-tastic'!",
        "What do you call an owl in the garden? A 'wise' gardener!",
    ],
}

_VALID_CATEGORIES = set(JOKES.keys())


def owl_joke(topic: str = "wise") -> str:
    """Return a random owl-themed joke from the specified category.

    Args:
        topic: The theme of the joke. One of ``"wise"``, ``"funny"``,
            ``"programming"``, or ``"nature"``.
            Defaults to ``"wise"``.

    Returns:
        A string containing one owl joke.

    Raises:
        ValueError: If *topic* is not recognised.
    """
    if topic not in _VALID_CATEGORIES:
        raise ValueError(
            f"Unknown topic: {topic!r}. "
            f"Choose from: {sorted(_VALID_CATEGORIES)}"
        )
    return random.choice(JOKES[topic])


def get_owl_joke(topic: str, index: int) -> str:
    """Return an owl joke from the specified category by index.

    Args:
        topic: The category of jokes.
        index: The index of the joke (0-based).

    Returns:
        The joke string.

    Raises:
        ValueError: If category is invalid or index out of range.
    """
    if topic not in _VALID_CATEGORIES:
        raise ValueError(f"Unknown topic: {topic!r}. Choose from: {sorted(_VALID_CATEGORIES)}")
    try:
        return JOKES[topic][index]
    except IndexError:
        raise ValueError(f"Index {index} out of range for topic {topic!r}")


def list_owl_jokes(topic: str = None) -> List[str]:
    """List all owl jokes in a category or all categories.

    Args:
        topic: The category to list, or None for all.

    Returns:
        List of joke strings.
    """
    if topic:
        if topic not in _VALID_CATEGORIES:
            return []
        return JOKES[topic]
    else:
        all_jokes = []
        for cat in JOKES.values():
            all_jokes.extend(cat)
        return all_jokes


def count_owl_jokes_in_category(topic: str) -> int:
    """Count the number of owl jokes in a category.

    Args:
        topic: The category to count.

    Returns:
        The number of jokes.

    Raises:
        ValueError: If category is invalid.
    """
    if topic not in _VALID_CATEGORIES:
        raise ValueError(f"Unknown topic: {topic!r}. Choose from: {sorted(_VALID_CATEGORIES)}")
    return len(JOKES[topic])