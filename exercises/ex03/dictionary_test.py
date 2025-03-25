import pytest
from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


def test_invert_use1() -> None:
    "Test that invert function inverts values"
    assert invert({"a": "1", "b": "2"}) == {"1": "a", "2": "b"}


def test_invert_use2() -> None:
    """Tests invert function with only 1 key and 1 value"""
    assert invert({"Austin": "Victoria"}) == {"Victoria": "Austin"}


def test_invert_edge1() -> None:
    """ensures that two original dictionary values returns KeyError"""
    with pytest.raises(KeyError):
        invert({"Hoka": "Nike", "New_Balance": "Nike", "Puma": "Nike"})


def test_count_use1() -> None:
    """Tests that count returns correct number of times used in a list"""
    assert count(["apple", "apple", "orange", "apple"]) == {"apple": 3, "orange": 1}


def test_count_use2() -> None:
    """Tests that count returns a dictionary from a list of 1 entry"""
    assert count(["knife"]) == {"knife": 1}


def test_count_edge1() -> None:
    """tests that an empty list input returns an empty dictionary output"""
    assert count([]) == {}


def test_favorite_color_use1() -> None:
    """Tests that favorite_color fn accurately returns most popular color"""
    assert (
        favorite_color(
            {
                "Jenny": "choc",
                "Austin": "choc",
                "Khamev": "choc",
                "Victoria": "mint",
                "Amy": "mint",
                "Shan": "none",
            }
        )
        == "choc"
    )


def test_favorite_color_use2() -> None:
    """Test that if tie, reports first color encountered"""
    assert (
        favorite_color({"mark": "blue", "jen": "red", "joe": "blue", "nia": "red"})
        == "blue"
    )


def test_favorite_color_edge1() -> None:
    "Test that an empty dictionary input returns an empty string literal"
    assert favorite_color({}) == ""


def test_bin_len_use1() -> None:
    """Tests that multpile length inputs in the list get sorted by length"""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_use2() -> None:
    """Tests that inputs of 1 length are listed in the same set in the dictionary"""
    assert bin_len(["red", "fox", "spy", "die"]) == {3: {"red", "fox", "spy", "die"}}


def test_bin_len_edge1() -> None:
    """Tests that input of empty list returns set literal"""
    assert bin_len([]) == {}
