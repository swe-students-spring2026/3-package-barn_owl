import pytest
from barn_owl import (
    count_owl_jokes_in_category,
    get_owl_joke,
    list_owl_jokes,
    owl_joke,
)


class TestOwlJoke:
    def test_owl_joke_valid_topic(self):
        joke = owl_joke("wise")
        assert isinstance(joke, str)
        assert joke in [
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
        ]

    def test_owl_joke_invalid_topic(self):
        with pytest.raises(ValueError):
            owl_joke("invalid")

    def test_owl_joke_default(self):
        joke = owl_joke()
        assert isinstance(joke, str)


class TestGetOwlJoke:
    def test_get_owl_joke_valid(self):
        joke = get_owl_joke("wise", 0)
        assert joke == "Why did the owl become a philosopher? Because it was wise to the ways of the night!"

    def test_get_owl_joke_invalid_topic(self):
        with pytest.raises(ValueError):
            get_owl_joke("invalid", 0)

    def test_get_owl_joke_invalid_index(self):
        with pytest.raises(ValueError):
            get_owl_joke("wise", 100)


class TestListOwlJokes:
    def test_list_owl_jokes_topic(self):
        jokes = list_owl_jokes("wise")
        assert len(jokes) == 10
        assert "Why did the owl become a philosopher? Because it was wise to the ways of the night!" in jokes

    def test_list_owl_jokes_all(self):
        jokes = list_owl_jokes()
        assert len(jokes) == 40  # 4 categories * 10

    def test_list_owl_jokes_invalid_topic(self):
        jokes = list_owl_jokes("invalid")
        assert jokes == []


class TestCountOwlJokesInCategory:
    def test_count_owl_jokes_valid(self):
        count = count_owl_jokes_in_category("wise")
        assert count == 10

    def test_count_owl_jokes_invalid(self):
        with pytest.raises(ValueError):
            count_owl_jokes_in_category("invalid")