import pytest

from barn_owl import to_owl_latin

class Tests:
    def test_simple_word(self):
        assert to_owl_latin("hello") == "ellohoo"

    def test_vowel_word(self):
        assert to_owl_latin("apple") == "applehoo"

    def test_sentence(self):
        assert to_owl_latin("hello world") == "ellohoo orldwoo"