import pytest

from barn_owl import owl_wisdom
from barn_owl.owl_wisdom import _VALID_TOPICS, _WISDOM


class TestOwlWisdomBasic:
    def test_returns_string(self):
        result = owl_wisdom.owl_wisdom()
        assert isinstance(result, str)

    def test_returns_non_empty_string(self):
        result = owl_wisdom.owl_wisdom()
        assert len(result) > 0

    def test_default_topic_is_life(self):
        for _ in range(20):
            result = owl_wisdom.owl_wisdom()
            assert result in _WISDOM["life"]


class TestOwlWisdomTopics:
    def test_life_topic(self):
        result = owl_wisdom.owl_wisdom(topic="life")
        assert result in _WISDOM["life"]

    def test_coding_topic(self):
        result = owl_wisdom.owl_wisdom(topic="coding")
        assert result in _WISDOM["coding"]

    def test_friendship_topic(self):
        result = owl_wisdom.owl_wisdom(topic="friendship")
        assert result in _WISDOM["friendship"]

    def test_nature_topic(self):
        result = owl_wisdom.owl_wisdom(topic="nature")
        assert result in _WISDOM["nature"]

    def test_food_topic(self):
        result = owl_wisdom.owl_wisdom(topic="food")
        assert result in _WISDOM["food"]

    def test_all_topics_have_at_least_one_quote(self):
        for topic in _VALID_TOPICS:
            assert len(_WISDOM[topic]) > 0

    def test_each_topic_returns_quote_from_correct_pool(self):
        for topic in _VALID_TOPICS:
            result = owl_wisdom.owl_wisdom(topic=topic)
            assert result in _WISDOM[topic]


class TestOwlWisdomErrors:
    def test_unknown_topic_raises_value_error(self):
        with pytest.raises(ValueError):
            owl_wisdom.owl_wisdom(topic="sports")

    def test_error_message_mentions_invalid_topic(self):
        with pytest.raises(ValueError, match="sports"):
            owl_wisdom.owl_wisdom(topic="sports")

    def test_error_message_lists_valid_topics(self):
        with pytest.raises(ValueError, match="life"):
            owl_wisdom.owl_wisdom(topic="bogus")

    def test_empty_string_topic_raises_value_error(self):
        with pytest.raises(ValueError):
            owl_wisdom.owl_wisdom(topic="")

    def test_case_sensitive_topic(self):
        with pytest.raises(ValueError):
            owl_wisdom.owl_wisdom(topic="Life")


class TestOwlWisdomRandomness:
    def test_repeated_calls_can_return_different_quotes(self):
        results = {owl_wisdom.owl_wisdom(topic="coding") for _ in range(50)}
        assert len(results) > 1
