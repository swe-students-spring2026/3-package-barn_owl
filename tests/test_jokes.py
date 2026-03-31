import pytest

from barn_owl import owl_jokes
from barn_owl.jokes import _VALID_CATEGORIES, _JOKES


class TestOwlJokesBasic:
    def test_returns_string(self):
        result = owl_jokes()
        assert isinstance(result, str)

    def test_returns_non_empty_string(self):
        result = owl_jokes()
        assert len(result) > 0

    def test_default_category_is_python(self):
        for _ in range(20):
            result = owl_jokes()
            assert result in _JOKES["python"]


class TestOwlJokesCategories:
    def test_python_category(self):
        result = owl_jokes(category="python")
        assert result in _JOKES["python"]

    def test_programming_category(self):
        result = owl_jokes(category="programming")
        assert result in _JOKES["programming"]

    def test_cold_category(self):
        result = owl_jokes(category="cold")
        assert result in _JOKES["cold"]

    def test_all_categories_have_at_least_one_joke(self):
        for category in _VALID_CATEGORIES:
            assert len(_JOKES[category]) > 0

    def test_each_category_returns_joke_from_correct_pool(self):
        for category in _VALID_CATEGORIES:
            result = owl_jokes(category=category)
            assert result in _JOKES[category]
            
    def test_invalid_category_raises_error(self):
        with pytest.raises(ValueError):
            owl_jokes(category="invalid_category")