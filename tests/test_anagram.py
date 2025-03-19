import pytest
import time
from anagram_package import anagram

        
@pytest.mark.parametrize("fill_word_invalid", [
    0,
    4,
    True,
    False,
    {"dictionary": "invalid"},
    [1, 2, 3],
    (lambda x: x+1)
])
def test_fill_word_invalid(fill_word_invalid: list[object]):
    # Tests for errors raised on invalid inputs
    with pytest.raises(Exception) as e:
        anagram.fill_word(fill_word_invalid)

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
