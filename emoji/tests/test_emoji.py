import pytest
from emoji import get_random_emoji, get_emoji, list_emojis, count_emojis


class TestGetRandomEmoji:
    def test_get_random_emoji_valid_category(self):
        emoji = get_random_emoji("happy")
        assert emoji in ["😊", "😂", "😄", "😃", "😀", "😁", "😆", "😅", "🤣", "🙂"]

    def test_get_random_emoji_invalid_category(self):
        with pytest.raises(ValueError):
            get_random_emoji("invalid")

    def test_get_random_emoji_default(self):
        emoji = get_random_emoji()
        assert emoji in ["😊", "😂", "😄", "😃", "😀", "😁", "😆", "😅", "🤣", "🙂"]


class TestGetEmoji:
    def test_get_emoji_known(self):
        assert get_emoji("smile") == "😊"
        assert get_emoji("heart") == "❤️"

    def test_get_emoji_unknown(self):
        assert get_emoji("unknown") == "unknown"


class TestListEmojis:
    def test_list_emojis_category(self):
        emojis = list_emojis("happy")
        assert len(emojis) == 10
        assert "😊" in emojis

    def test_list_emojis_all(self):
        emojis = list_emojis()
        assert len(emojis) == 40  # 4 categories * 10

    def test_list_emojis_invalid_category(self):
        emojis = list_emojis("invalid")
        assert emojis == []


class TestCountEmojis:
    def test_count_emojis_none(self):
        assert count_emojis("Hello world") == 0

    def test_count_emojis_some(self):
        assert count_emojis("I 😊 you ❤️") == 2

    def test_count_emojis_multiple_same(self):
        assert count_emojis("😊😊😊") == 3