import pytest
from anagram_package.__main__ import main

# mocking inputs
@pytest.fixture
def mock_inputs(monkeypatch):
    """Fixture to simulate user input"""
    def _mock_inputs(input_values):
        input_iter = iter(input_values)
        monkeypatch.setattr('builtins.input', lambda _: next(input_iter))
    return _mock_inputs

# fill_word Function Tests
# Test 1: Test with pattern having multiple blanks
def test_fill_word_function_multiple_blanks(mock_inputs, capsys):
    
    mock_inputs(['1', 'p_th_n', '5'])
    

    main()
        
    # capture output
    captured = capsys.readouterr()
    output = captured.out
    
    # Verify output
    assert "Fill in missing letters in a word pattern" in output
    assert "Found" in output
    assert "python" in output.lower()

# Test 2: Test with pattern having single blank
def test_fill_word_multiple_basic(mock_inputs, capsys):

    mock_inputs(['1', 'c_t', '5'])
    
    main()
    
    # capture output
    captured = capsys.readouterr()
    output = captured.out
    
    # Verify output
    assert "Fill in missing letters in a word pattern" in output
    assert "Found" in output
    assert any(word in output.lower() for word in ["cat", "cot", "cut"])

# Test 3: Test with pattern that has no matches
def test_fill_word_no_matches(mock_inputs, capsys):
    mock_inputs(['1', 'xyzxyz___', '5'])
    
    main()
    
    # capture output
    captured = capsys.readouterr()
    output = captured.out
    
    # Verify output
    assert "Fill in missing letters in a word pattern" in output
    assert "No matching words found" in output

# Create Anagram Function Tests
# Test 1: Test with a basic word
def test_create_anagram_function_basic(mock_inputs, capsys):
    mock_inputs(['2', 'listen', '5'])
    
    main()
        
    # capture output
    captured = capsys.readouterr()
    output = captured.out
    
    # Verify output
    assert "Create anagrams from a word" in output
    assert "silent" in output.lower()

# Test 2: Test with a single letter word (no anagrams)
def test_create_anagram_single_letter(mock_inputs, capsys):
    mock_inputs(['2', 'a', '5'])
    
    main()
    
    # capture output
    captured = capsys.readouterr()
    output = captured.out
    
    # Verify output
    assert "Create anagrams from a word" in output
    assert "No anagrams found" in output

# Test 3: Test with a word that has multiple anagrams
def test_create_anagram_multiple_results(mock_inputs, capsys):
    mock_inputs(['2', 'post', '5'])
    
    main()
        
    # capture output
    captured = capsys.readouterr()
    output = captured.out
    
    # Verify output
    assert "Create anagrams from a word" in output
    assert "Found" in output
    assert any(word in output.lower() for word in ["stop", "tops", "opts", "spot"])

# Check Anagram Function Tests
# Test 1: Test with words that are anagrams
def test_check_anagram_true(mock_inputs, capsys):
    mock_inputs(['3', 'listen', 'silent', '5'])
    
    main()
        
    # capture output
    captured = capsys.readouterr()
    output = captured.out
    
    # Verify output
    assert "Check if two words are anagrams" in output
    assert "'listen' and 'silent' are anagrams" in output

# Test 2: Test with words that are not anagrams
def test_check_anagram_false(mock_inputs, capsys):
    mock_inputs(['3', 'hello', 'world', '5'])
    
    main()
    
    # capture output
    captured = capsys.readouterr()
    output = captured.out
    
    # Verify output
    assert "Check if two words are anagrams" in output
    assert "'hello' and 'world' are NOT anagrams" in output

# Test 3: Test with words that are anagrams but with different cases
def test_check_anagram_case_insensitive(mock_inputs, capsys):
    mock_inputs(['3', 'Listen', 'SiLenT', '5'])
    
    main()
    
    # capture output
    captured = capsys.readouterr()
    output = captured.out
    
    # Verify output
    assert "Check if two words are anagrams" in output
    assert "'Listen' and 'SiLenT' are anagrams" in output

# Filter Palindromes Function Tests
# Test 1: Test with some palindromes and non-palindromes
def test_filter_palindromes_basic(mock_inputs, capsys):
    mock_inputs(['4', 'radar level python', '3', '5'])
    
    main()
    
    # capture output
    captured = capsys.readouterr()
    output = captured.out
    
    # Verify output
    assert "Find palindromes in a list of words" in output
    assert "Found" in output
    assert "radar" in output
    assert "level" in output
    assert "python" not in output.split("Found")[1]  # python is not a palindrome

# Test 2: Test with minimum length filter
def test_filter_palindromes_min_length(mock_inputs, capsys):
    mock_inputs(['4', 'a aa madam', '3', '5'])
    
    main()
    
    #capture output
    captured = capsys.readouterr()
    output = captured.out
    
    # Verify output
    assert "Find palindromes in a list of words" in output
    assert "Found" in output
    assert "madam" in output
    assert output.count("madam") == 1
    assert output.count("Found 1 palindrome") == 1

# Test 3: Test with no palindromes
def test_filter_palindromes_no_matches(mock_inputs, capsys):
    mock_inputs(['4', 'hello world python', '3', '5'])
    
    main()
        
    # capture output
    captured = capsys.readouterr()
    output = captured.out
    
    # Verify output
    assert "Find palindromes in a list of words" in output
    assert "No palindromes" in output

# Test 4: Test with non-numeric minimum length input
def test_filter_palindromes_non_numeric_min_length(mock_inputs, capsys):
    # should default to 3 if non-numeric input is provided
    mock_inputs(['4', 'radar level', 'abc', '5'])
    
    main()
    
    # capture output
    captured = capsys.readouterr()
    output = captured.out
    
    # Verify output
    assert "Find palindromes in a list of words" in output
    assert "radar" in output
    assert "level" in output

# Menu Option Tests
# Test 1: Test with invalid option
def test_invalid_option(mock_inputs, capsys):
    mock_inputs(['8', '5'])

    main()
        
    # capture output
    captured = capsys.readouterr()
    output = captured.out
    
    # Verify error message
    assert "Invalid choice" in output

# Test 2: Test with exit option
def test_exit_option(mock_inputs, capsys):
    mock_inputs(['5'])
    
    main()
    
    # capture output
    captured = capsys.readouterr()
    output = captured.out
    
    # Happy spring break!
    assert "Happy spring break!" in output 