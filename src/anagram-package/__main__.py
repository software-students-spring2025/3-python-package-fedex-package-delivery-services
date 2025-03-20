import anagram_package.anagram as anagram

def main():
    print("Welcome to the Anagram game!")
    
    # Load the word list
    words = anagram.load_word_list()
    print(f"Loaded dictionary with {len(words)} words.")
    
    while True:
        print("\nChoose from the following options:")
        print("1. Fill in missing letters in a word pattern")
        print("2. Create anagrams from a word")
        print("3. Check if two words are anagrams")
        print("4. Find palindromes in a list of words")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            pattern = input("Enter a word pattern with underscores for missing letters (e.g. 'p_th_n'): ")
            results = anagram.fill_word(pattern)
            if results:
                print(f"Found {len(results)} matching words:")
                for word in results[:20]:
                    print(f"  {word}")
                if len(results) > 20:
                    print(f"  ...and {len(results) - 20} more")
            else:
                print("No matching words found.")
                
        elif choice == "2":
            word = input("Enter a word to find anagrams for: ")
            anagrams = anagram.create_anagram(word)
            if anagrams:
                print(f"Found {len(anagrams)} anagrams:")
                for anagram_word in anagrams[:20]:
                    print(f"  {anagram_word}")
                if len(anagrams) > 20:
                    print(f"  ...and {len(anagrams) - 20} more")
            else:
                print("No anagrams found.")
                
        elif choice == "3":
            word1 = input("Enter the first word: ")
            word2 = input("Enter the second word: ")
            if anagram.check_anagram(word1, word2):
                print(f"'{word1}' and '{word2}' are anagrams!")
            else:
                print(f"'{word1}' and '{word2}' are NOT anagrams.")
                
        elif choice == "4":
            word_input = input("Enter a few words separated by spaces: ")
            min_length = input("Enter minimum length for palindromes: ")
            min_length = int(min_length) if min_length.isdigit() else 3
            
            word_list = word_input.split()
            palindromes = anagram.filter_palindromes(word_list, min_length)
            
            if palindromes:
                print(f"Found {len(palindromes)} palindromes:")
                for p in palindromes:
                    print(f"  {p}")
            else:
                print(f"No palindromes of length {min_length} or greater found.")
                
        elif choice == "5":
            print("Happy spring break!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()