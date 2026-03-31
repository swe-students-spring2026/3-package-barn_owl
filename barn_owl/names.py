import random

_OWL_NAMES: dict[str, dict[str, list[str]]] = {
    "wise": {
        "first": [
            "Barnaby",
            "Athena",
            "Eldric",
            "Sagewing",
            "Noctis",
            "Morrow",
        ],
        "titles": [
            "Moonwatcher",
            "Star Reader",
            "Old Oak Seer",
            "Night Scholar",
            "Silent Oracle",
            "Keeper of Twilight",
        ],
    },
    "spooky": {
        "first": [
            "Grimsworth",
            "Hexa",
            "Rook",
            "Mourn",
            "Vesper",
            "Shade",
        ],
        "titles": [
            "Cursed",
            "Crypt Caller",
            "Hollow Hooter",
            "Grave Percher",
            "Lantern Stalker",
            "Fogbound",
        ],
    },
    "cute": {
        "first": [
            "Pip",
            "Muffin",
            "Nibbles",
            "Tilly",
            "Bean",
            "Bubbles",
        ],
        "titles": [
            "Snugglefeather",
            "Button Eyes",
            "Tiny Talons",
            "Cuddlefluff",
            "Dewdrop",
            "Peep Peep",
        ],
    },
    "funny": {
        "first": [
            "Hootie",
            "Sir Flaps",
            "Wobble",
            "Pickles",
            "Professor Bonk",
            "Noodle",
        ],
        "titles": [
            "Unbothered",
            "Snack Inspector",
            "Branch Manager",
            "Feather Comedian",
            "Pajama Pilot",
            "Chief Hoot Officer",
        ],
    },
}

_VALID_STYLES = set(_OWL_NAMES.keys())


def owl_name_generator(style: str = "wise") -> str:
    """Return a random owl name for a given style.

    Args:
        style: The naming style to use. One of "wise", "spooky",
            "cute", or "funny". Defaults to "wise".

    Returns:
        A full owl name string in the form "[first] the [title]".

    Raises:
        ValueError: If style is not recognized.
    """

    if style not in _VALID_STYLES:
        raise ValueError(
            f"Unknown style: {style!r}. "
            f"Choose from: {sorted(_VALID_STYLES)}"
        )

    return f"{random.choice(_OWL_NAMES[style]['first'])} the {random.choice(_OWL_NAMES[style]['titles'])}"