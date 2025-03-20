import pytest
import time
from anagram_package import anagram

@pytest.fixture
def non_string_inputs():
        return ([
        0,
        4,
        True,
        False,
        {"dictionary": "invalid"},
        [1, 2, 3],
        (lambda x: x+1)
    ])

def test_fill_word_invalid(non_string_inputs):
    # Tests for errors raised on invalid inputs
    with pytest.raises(Exception) as e:
        anagram.fill_word(non_string_inputs)

@pytest.mark.parametrize("fill_word_expected", [
    ("", [""]),
    ("a", ["a"]),
    ("b_ll", ["ball", "bell", "bill", "boll", "bull"]),
    ("z_w", []),
    ("art__le", ["article"]),
    ("pr_b_bili__", ["probability"]),
])
def test_fill_word_valid(fill_word_expected):
    # Tests to make sure expected outputs match
    assert(anagram.fill_word(fill_word_expected[0]).sort() == fill_word_expected[1].sort())

def test_fill_word_efficiency():
    # Tests the speed of fill_word
    for i in range(1, 100):
        start_time = time.perf_counter()
        anagram.fill_word("_" * i)
        end_time = time.perf_counter()
        # Arbitrary linear asymptote O(n) just to make sure
        # it's not atrociously slow. Unlikely a word ever is greater than
        # 100 characters
        assert(end_time - start_time < i)


def test_create_anagram_invalid(non_string_inputs):
    # Tests for errors raised on invalid inputs
    with pytest.raises(Exception) as e:
        anagram.fill_word(non_string_inputs)

@pytest.mark.parametrize("create_anagram_expected", [
     ("", []),
     ("a", ["a"]),
     ("bore", ["boer", "robe"]),
     ("purple", ["pulper", "repulp"]),
     ("broken", [])
])
def test_create_anagram_valid(create_anagram_expected):
    # Tests expected outputs on create_anagram
    assert(anagram.create_anagram(create_anagram_expected[0]).sort() == create_anagram_expected[1].sort())

def test_create_anagram_non_alpha_chars():
    # Tests that the output of strings with non-alphabetic characters are empty
    assert(anagram.create_anagram("bat@") == [])
    assert(anagram.create_anagram("bat\n") == [])
    assert(anagram.create_anagram("bat\r") == [])
    assert(anagram.create_anagram("bat5") == [])


@pytest.mark.parametrize("check_anagram_invalid_inputs", [
    (5, 5),
    ("h", 5),
    (5, "h"),
    ("h", True),
    (False, "h"),
    ("h", {"test": "test"}),
    ({"test": "test"}, "h"),
    ("h", ["h", "h"]),
    (["h", "h"], "h")
])
def test_check_anagram_invalid(check_anagram_invalid_inputs):
    with pytest.raises(Exception) as e:
        anagram.check_anagram(*non_string_inputs)

@pytest.mark.parametrize("check_anagram_matches", [
    ("", ""),
    ("h", "h"),
    ("asdf", "adsf"),
    ("asdf", "asfd"),
    ("asdf", "fads"),
    ("aaaa", "aaaa"),
    ("asdfghjkl", "lkjhgfdsa")
])
def test_check_anagram_matches(check_anagram_matches):
    assert(anagram.check_anagram(*check_anagram_matches))

@pytest.mark.parametrize("check_anagram_non_matches", [
    ("", "h"),
    ("h", ""),
    ("asdf", "asdfg"),
    ("asdfg", "gfds"),
    ("hh", "h")
])
def test_check_anagram_non_matches(check_anagram_non_matches):
    assert(not anagram.check_anagram(*check_anagram_non_matches))
