import pytest 

from barn_owl import owl_drawing 
from barn_owl.drawing import _DRAWING, _VALID_STYLES 

class TestOwlDrawingBasic:
    def test_returns_string(self):
        result = owl_drawing()
        assert isinstance(result, str)

    def test_returns_non_empty_string(self):
        result = owl_drawing()
        assert len(result) > 0

    def test_no_style_is_only_whitespace(self):
        result = owl_drawing()
        assert result.strip() != ""

    def test_default_style_is_cute(self):
        for _ in range(20):
            result = owl_drawing()
            assert result in _DRAWING["cute"]

class TestOwlDrawingStyles:
    def test_wise_style(self):
        result = owl_drawing(style="wise")
        assert result in _DRAWING["wise"]

    def test_cute_style(self):
        result = owl_drawing(style="cute")
        assert result in _DRAWING["cute"]

    def test_spooky_style(self):
        result = owl_drawing(style="spooky")
        assert result in _DRAWING["spooky"]

    def test_funny_style(self):
        result = owl_drawing(style="funny")
        assert result in _DRAWING["funny"]

    def test_large_style(self):
        result = owl_drawing(style="large")
        assert result in _DRAWING["large"]

    def test_duo_style(self):
        result = owl_drawing(style="duo")
        assert result in _DRAWING["duo"]

    def test_emoji_style(self):
        result = owl_drawing(style="emoji")
        assert result in _DRAWING["emoji"]

    def test_all_styles_have_at_least_one_drawing(self):
        for styles in _VALID_STYLES:
            assert len(_DRAWING[topic]) > 0

    def test_each_style_returns_drawing_from_correct_pool(self):
        for style in _VALID_STYLES:
            result = owl_drawing(style=style)
            assert result in _DRAWING[style]
    
    def test_drawings_are_not_identical_within_style(self):
        for style in _VALID_STYLES:
            results = _DRAWING[style]
            if len(results) > 1:
                assert len(set(results)) > 1

class TestOwlDrawingErrors:
    def test_unknown_style_raises_value_error(self):
        with pytest.raises(ValueError):
            owl_drawing(style="angry")

    def test_error_message_mentions_invalid_style(self):
        with pytest.raises(ValueError, match="angry"):
            owl_drawing(style="angry")

    def test_error_message_lists_valid_styles(self):
        with pytest.raises(ValueError, match="cute"):
            owl_drawing(style="bogus")

    def test_empty_string_style_raises_value_error(self):
        with pytest.raises(ValueError):
            owl_drawing(style="")

    def test_case_sensitive_style(self):
        with pytest.raises(ValueError):
            owl_drawing(style="Wise")


class TestOwlDrawingRandomness:
    def test_repeated_calls_can_return_different_drawing(self):
        results = {owl_drawing(style="funny") for _ in range(50)}
        assert len(results) > 1