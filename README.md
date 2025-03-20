# Anagram

![Python build & test](https://github.com/software-students-spring2025/3-python-package-fedex-package-delivery-services/actions/workflows/build.yml/badge.svg)

## [Anagram on PyPi](+LATER+)

## Getting Started with Anagram
First install anagram using the following command:
`pip install ` +LATER+

To import anagram into your code, use:
`from anagram_package import anagram`

## Features

#### `fill_word(pattern)`

- `pattern`: a string containing a word's known characters and `"_"` characters designating empty spaces

Returns a list of words that could be made by filling characters into the empty spaces marked by `"_"` in argument `pattern`

```
from anagram_package import anagram

# Returns "article"
anagram.fill_word("art__le")
```


#### `create_anagram(word)` 

- `word`: a string containing the word (or arbitrary characters) that will make up the anagram

Returns a list of words that are anagrams of `word`, meaning they share the same characters in the same respective quantities

```
from anagram_package import anagram

# Returns ["pulper", "repulp"]
anagram.create_anagram("purple")
```

#### `check_anagram(word1, word2)`

- `word1`: A string with a word
- `word2`: A string with a word to compare to `word1` for anagram status

Returns a `bool` indicating whether or not `word1` and `word2` are anagrams of each other

```
from anagram_package import anagram

# Returns True
anagram.check_anagram("bat", "tab")

# Returns False
anagram.check_anagram("bat", "artichoke")
```

#### `filter_palindromes(words, min_length)`