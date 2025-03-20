![Python build & test](https://github.com/software-students-spring2025/3-python-package-fedex-package-delivery-services/actions/workflows/build.yml/badge.svg)

# Anagram Package
A package that contains a collection of playful word based functions, allowing you generate and check anagrams, as well as solve missing letter puzzles and find palindromes!

[PyPI link](https://pypi.org/project/anagram-package/)
Authors:
- [Isaac Fisher](https://github.com/isaac1000000)
- [Wyatt Destabelle](https://github.com/Wyatt-Destabelle)
- [Alan Chen](https://github.com/Chen-zexi)
- [Nick Michael](https://github.com/NMichael111)
## Installation

Install this package using pip: \
`pip install --upgrade anagram-package`

## Running the Package

### Option 1: Use the command-line interface

Type the following in your terminal to launch the interactive menu:

`
anagram_package
`

### Option 2: Run as a Python module

You can also run the package as a Python module:

`
python -m anagram_package
`

### Option 3: Import into your Python code

```
from anagram_package.anagram import fill_word, create_anagram, check_anagram, filter_palindromes
```


## Functions
This Program currently contains four functions:
1. fill_word(pattern): This takes a String containing one word with any number of letters replaced with an underscore '_', and returns all words that could fill the gap. eg. "Pyt_on" would return "Python".
    - Parameters:
        - `pattern`: Required. A String containing only one word (no spaces), with any amount of letters replaced with an underscore ('_'). 
    - Return: Returns a list of strings, respresenting all words that could fill the missing spaces in the word given in `pattern`.
2. create_anagram(word): This takes a String containing one word, and returns a list of strings containing every anagram of that word.
   - Parameters:
        - `word`: Required. A String containing only one word (no spaces).
    - Return: Returns a list of strings, respresenting anagrams of the word entered in `word`.
3. check_anagram(word1,word2): This takes two strings, each containing one word (no spaces), and checks if they are anagrams of each other. It will return a boolean of the result of the comparision.
    - Parameters:
        - `word1`: Required. A String containing only one word (no spaces).
        - `word2`: Required. A String containing only one word (no spaces).
    - Return: Returns a boolean, which is true if `word1` and `word2` are anagrams, and false if not.
4. filter_palindromes(words): Takes a list of Strings each containing only one word (no spaces), and returns a list of the words that are palindromes.
   - Parameters:
        - `words`: Required. A List of Strings each containing only one word (no spaces).
   - Return: Retursn a list of Strings containing all the Strings from `words` that are palindromic.

## Program Usage Example 
[Example Program](https://github.com/software-students-spring2025/3-python-package-fedex-package-delivery-services/blob/main/anagram_package/__main__.py)

## Contributions

Please preform the following steps if you wish to make a contribution to the project:
1. Fork this repository:
    - `git clone https://github.com/software-students-spring2025/3-python-package-fedex-package-delivery-services.git`
2. Enter the directory:
    - `cd 3-python-package-fedex-package-delivery-services`
3. Create a new branch for your changes.
4. Set up a virtual enviroment and install dependencies:
    - `pipenv install` \
`pipenv shell`
5. Write your changes!
5. Build the package:
    - `pipenv run python -m build`
6. After you have built your changes, run the unit tests included within the project (please include new unit tests for any new or changed functions):
    - `pipenv run python -m pytest tests/`
7. Submit a pull request on github so we can review your changes!
