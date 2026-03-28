"""
Tests for owl latin functions.
"""

import pytest

from barn_owl import to_owl_latin

class TestOwlLatinBasic:
    def test_empty_string(self):
        assert to_owl_latin("") == ""

    def test_whitespace_only(self):
        assert to_owl_latin("   ") == ""

    def test_single_letter_vowel(self):
        assert to_owl_latin("a") == "ahoo"

    def test_single_letter_consonant(self):
        assert to_owl_latin("b") == "boo"

class TestOwlLatinTranslations:
    def test_simple_word(self):
        assert to_owl_latin("hello") == "ellohoo"

    def test_vowel_word(self):
        assert to_owl_latin("apple") == "applehoo"

    def test_sentence(self):
        assert to_owl_latin("hello world") == "ellohoo orldwoo"

    def test_capitalization_preserved(self):
        assert to_owl_latin("Hello") == "elloHoo"

    def test_multiple_consonants(self):
        assert to_owl_latin("string") == "ingstroo"

    def test_no_vowels(self):
        assert to_owl_latin("syzygy") == "syzygyoo"


class TestOwlLatinPunctuation:
    def test_word_with_period(self):
        assert to_owl_latin("hello.") == "ellohoo."

    def test_word_with_comma(self):
        assert to_owl_latin("hello,") == "ellohoo,"

    def test_quotes(self):
        assert to_owl_latin('"hello"') == '"ellohoo"'

    def test_parentheses(self):
        assert to_owl_latin("(hello)") == "(ellohoo)"

    def test_mixed_punctuation_sentence(self):
        assert to_owl_latin("Hello, world!") == "elloHoo, orldwoo!"

    def test_only_punctuation(self):
        assert to_owl_latin("!!!") == "!!!"

class TestOwlLatinEdgeCases:
    def test_mixed_case_word(self):
        assert to_owl_latin("hElLo") == "ElLohoo"

    def test_numbers_in_word(self):
        assert to_owl_latin("h3llo") == "3llohoo"

    def test_numbers_start_word(self):
        assert to_owl_latin("2pac") == "2pachoo"

    def test_hyphenated_word(self):
        assert to_owl_latin("hello-world") == "ello-worldhoo"

    def test_multiple_spaces_between_words(self):
        assert to_owl_latin("hello   world") == "ellohoo orldwoo"

    def test_newlines(self):
        assert to_owl_latin("hello\nworld") == "ellohoo orldwoo"

class TestOwlLatinTypes:
    def test_non_string_input_int(self):
        with pytest.raises(TypeError):
            to_owl_latin(123)

    def test_non_string_input_list(self):
        with pytest.raises(TypeError):
            to_owl_latin(["hello", "world"])

    def test_non_string_input_none(self):
        with pytest.raises(TypeError):
            to_owl_latin(None)