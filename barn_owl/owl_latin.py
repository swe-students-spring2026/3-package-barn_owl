import string


def to_owl_latin(text: str) -> str:
    """Convert text to Owl Latin.

    Words starting with a vowel get ``hoo`` appended. Otherwise leading
    consonants move after the first vowel and ``oo`` is appended.
    Punctuation at the edges of a word is preserved.
    """
    vowels = "aeiou"
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

        first_vowel_idx = 0
        for i, char in enumerate(word):
            if char.lower() in vowels:
                first_vowel_idx = i
                break

        if word[0].lower() in vowels:
            new_word = word + "hoo"
        else:
            new_word = word[first_vowel_idx:] + word[:first_vowel_idx] + "oo"

        result.append(prefix + new_word + suffix)

    return " ".join(result)