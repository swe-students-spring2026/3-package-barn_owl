"""
Contains all functions related to owl latin.
"""

import string

def to_owl_latin(text: str = "") -> str:
    """
    Convert a string of text into owl latin. Append 'hoo' to words starting with a non-consonant,
    otherwise, move leading consonants to the end and append 'oo'. Keep all leading and trailing
    punctuation as-is.

    Args:
        text: The text to be translated to owl latin. Defaults to an empty string.

    Returns:
        A string containing the input string translated to owl latin.

    Raises:
        TypeError: If *text* is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("Text must be a string.")

    consonants = "qwrtypsdfghjklzxcvbnm"
    words = text.split()
    result = []

    for word in words:
        prefix = ""
        suffix = ""

        while word and word[0] in string.punctuation:
            prefix += word[0]
            word = word[1:]

        while word and word[-1] in string.punctuation:
            suffix = word[-1] + suffix
            word = word[:-1]

        if not word:
            result.append(prefix + suffix)
            continue

        first_non_consonant_idx = None
        for i, char in enumerate(word):
            if char.lower() not in consonants:
                first_non_consonant_idx = i
                break

        if word[0].lower() not in consonants:
            new_word = word + "hoo"
        elif first_non_consonant_idx is None:
            new_word = word + "oo"
        else:
            new_word = word[first_non_consonant_idx:] + word[:first_non_consonant_idx] + "oo"

        result.append(prefix + new_word + suffix)

    return " ".join(result)