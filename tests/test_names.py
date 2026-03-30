import pytest

from barn_owl import owl_name_generator
from barn_owl.names import _OWL_NAMES, _VALID_STYLES


class TestOwlNameGeneratorBasic:
    def test_returns_string(self):
        res = owl_name_generator()
        assert isinstance(res, str)

    def test_returns_non_empty_string(self):
        res = owl_name_generator()
        assert len(res) > 0

    def test_default_style_is_wise(self):
        for i in range(20):
            res = owl_name_generator()
            firstname, title = res.split(" the ", 1)
            assert firstname in _OWL_NAMES["wise"]["first"]
            assert title in _OWL_NAMES["wise"]["titles"]


class TestOwlNameGeneratorStyles:
    def test_wise_style(self):
        res = owl_name_generator(style="wise")
        firstname, title = res.split(" the ", 1)
        assert firstname in _OWL_NAMES["wise"]["first"]
        assert title in _OWL_NAMES["wise"]["titles"]
        assert isinstance(res, str)

    def test_spooky_style(self):
        res = owl_name_generator(style="spooky")
        firstname, title = res.split(" the ", 1)
        assert firstname in _OWL_NAMES["spooky"]["first"]
        assert title in _OWL_NAMES["spooky"]["titles"]
        assert isinstance(res, str)

    def test_cute_style(self):
        res = owl_name_generator(style="cute")
        firstname, title = res.split(" the ", 1)
        assert firstname in _OWL_NAMES["cute"]["first"]
        assert title in _OWL_NAMES["cute"]["titles"]
        assert isinstance(res, str)

    def test_funny_style(self):
        res = owl_name_generator(style="funny")
        firstname, title = res.split(" the ", 1)
        assert firstname in _OWL_NAMES["funny"]["first"]
        assert title in _OWL_NAMES["funny"]["titles"]
        assert isinstance(res, str)

    def test_each_valid_style_works_without_error(self):
        for style in _VALID_STYLES:
            res = owl_name_generator(style=style)
            firstname, title = res.split(" the ", 1)
            assert firstname in _OWL_NAMES[style]["first"]
            assert title in _OWL_NAMES[style]["titles"]
            assert isinstance(res, str)


class TestOwlNameGeneratorErrors:
    
    def test_invalid_style_raises_value_error(self):
        with pytest.raises(ValueError):
            owl_name_generator(style="royal")

    def test_error_message_mentions_invalid_style(self):
        with pytest.raises(ValueError, match="royal"):
            owl_name_generator(style="royal")

    def test_error_message_lists_valid_options(self):
        with pytest.raises(ValueError, match="wise"):
            owl_name_generator(style="unknown")
