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
   
# Tests for errors raised on invalid inputs
def test_fill_word_invalid(non_string_inputs):
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
# Tests to make sure expected outputs match
def test_fill_word_valid(fill_word_expected):
    assert(anagram.fill_word(fill_word_expected[0]).sort() == fill_word_expected[1].sort())

# Tests the speed of fill_word
def test_fill_word_efficiency():
    for i in range(1, 50):
        start_time = time.perf_counter()
        anagram.fill_word("_" * i)
        end_time = time.perf_counter()
        # Arbitrary linear asymptote O(n) just to make sure
        # it's not atrociously slow. Unlikely a word ever is greater than
        # 50 characters
        assert(end_time - start_time < i)

# Tests for errors raised on invalid inputs
def test_create_anagram_invalid(non_string_inputs):
    with pytest.raises(Exception) as e:
        anagram.fill_word(non_string_inputs)

@pytest.mark.parametrize("create_anagram_expected", [
     ("", []),
     ("a", ["a"]),
     ("bore", ["boer", "robe"]),
     ("purple", ["pulper", "repulp"]),
     ("broken", [])
])
# Tests expected outputs on create_anagram
def test_create_anagram_valid(create_anagram_expected):
    assert(anagram.create_anagram(create_anagram_expected[0]).sort() == create_anagram_expected[1].sort())
    
# Tests that the output of strings with non-alphabetic characters are empty
def test_create_anagram_non_alpha_chars():
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
# Tests for errors thrown on invalid inputs
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
# Tests for expected matches
def test_check_anagram_matches(check_anagram_matches):
    assert(anagram.check_anagram(*check_anagram_matches))

@pytest.mark.parametrize("check_anagram_non_matches", [
    ("", "h"),
    ("h", ""),
    ("asdf", "asdfg"),
    ("asdfg", "gfds"),
    ("hh", "h")
])
# Tests for expected non-matches
def test_check_anagram_non_matches(check_anagram_non_matches):
    assert(not anagram.check_anagram(*check_anagram_non_matches))

@pytest.mark.parametrize("filter_palindromes_invalid", [
    (["a", "b", "c"], [1, 2, 3]),
    (1, 1),
    ([1, 1, 1], 1),
    (True, 1)
])
# Tests for errors on invalid input to test_filter
def test_filter_palindromes_invalid(filter_palindromes_invalid):
    with pytest.raises(Exception) as e:
        anagram.filter_palindromes(*filter_palindromes_invalid)

@pytest.mark.parametrize("filter_palindromes_expected", [
    (["asdfdsa", "asdfds"], 2, ["asdfdsa"]),
    (["asdfdsa", "asdfds"], 7, ["asdfdsa"]),
    (["asdfdsa", "asdfds"], 8, []),
    ([], 0, []),
    (["asdfdsa", "asdfds", "mnbvbnm"], 2, ["asdfdsa", "mnbvbnm"]),
    (["asdffdsa", "asdfds"], 2, ["asdffdsa"]),
    (["asdffdsa", "asdfds"], 8, ["asdffdsa"]),
    (["asdffdsa", "asdfds"], 9, ["asdffdsa"]),
])
# Test results of test_filter against expected
def test_filter_palindromes_expected(filter_palindromes_expected):
    args = filter_palindromes_expected[:2]
    expected = filter_palindromes_expected[2]
    assert(anagram.filter_palindromes(*args).sort() == expected.sort())

# Tests the efficiency of filter_palindromes
def test_filter_palindromes_efficiency():
    for i in range(1, 200):
        start_time = time.perf_counter()
        anagram.filter_palindromes("a" * i)
        end_time = time.perf_counter()
        # Arbitrary linear asymptote O(n), unlikely a word's length 
        # is ever greater than 200 characters
        assert(end_time - start_time < i)