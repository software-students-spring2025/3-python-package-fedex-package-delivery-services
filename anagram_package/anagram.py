import pickle
import time
from typing import List, Set
import os

_WORD_CACHE = None

def load_word_list() -> Set[str]:
    global _WORD_CACHE
    if _WORD_CACHE is not None:
        return _WORD_CACHE
    try:
        with open(os.path.join(os.path.dirname(__file__), "words.pkl"), 'rb') as f:
            _WORD_CACHE = pickle.load(f)
        return _WORD_CACHE
    except (FileNotFoundError, pickle.UnpicklingError):
        print("Dictionary file not found or corrupted.")
        return set() 

# Takes a word with one or more letters missing "Pyt_on" and returns all possible words that could fill the gaps
def fill_word(pattern: str) -> List[str]:
    start_time = time.perf_counter()
    pattern = pattern.lower()
    pattern_length = len(pattern)
    words = load_word_list()
    
    result = [word for word in words if len(word) == pattern_length and all(
        p == '_' or p == w for p, w in zip(pattern, word)
    )]
    
    end_time = time.perf_counter()
    print(f"fill_word took {end_time - start_time:.6f} seconds")
    return result

# Takes a word and returns all of its anagrams
def create_anagram(word: str) -> List[str]:
    words = load_word_list()
    if not words:
        print("words is None")
        return []
    sorted_word = ''.join(sorted(word))  
    sorted_words = {}
    for w in words:
        key = ''.join(sorted(w))
        sorted_words.setdefault(key, []).append(w)
    return [w for w in sorted_words.get(sorted_word, []) if w != word]

# Check if two words are anagrams
def check_anagram(word1: str, word2: str) -> bool:
    return sorted(word1.lower()) == sorted(word2.lower())

# Takes a list of words and returns those which are palindromes
def filter_palindromes(words: List[str], min_length: int = 3) -> List[str]:
    return [word for word in words if len(word) >= min_length and word == word[::-1]]
