# Strings - A Collection of String Manipulation Functions

This repository provides a collection of Python functions for various string manipulations, covering common tasks and algorithms.  It serves as a handy resource for string-related operations and can be used as a learning tool or a quick reference.

## Features

This library includes functions for:

* **Basic Manipulations:** Reversing, checking for palindromes, counting vowels/consonants, case conversion.
* **Advanced Operations:** Removing duplicates, finding substrings, string formatting, and more.
* **Encoding/Decoding:** (If applicable, mention encoding/decoding related functions here)
* **Regular Expressions:** (If applicable, mention functions using regular expressions)

## Functions

Here's a glimpse of some key functions:

* **`reverse_string(s)`:** Reverses the input string `s`.  Supports various character sets.
* **`is_palindrome(s, case_insensitive=True)`:** Checks if `s` is a palindrome.  `case_insensitive` option allows for case-insensitive comparison.
* **`count_vowels(s)` / `count_consonants(s)`:** Counts vowels or consonants in `s`.
* **`remove_duplicates(s, preserve_order=True)`:** Removes duplicate characters. `preserve_order` maintains the original order of unique characters.
* **`find_substring(s, sub)`:** Finds the first occurrence of substring `sub` in `s`.
* **`format_string(s, *args, **kwargs)`:**  Provides custom string formatting (similar to Python's built-in `format()`).
* **`capitalize_words(s)`:** Capitalizes the first letter of each word in the string.

(Add more functions and their descriptions as needed)

## Usage

```python
from strings import reverse_string, is_palindrome, count_vowels, remove_duplicates, capitalize_words

my_string = "Hello World!"

print(reverse_string(my_string))       # Output: !dlroW olleH
print(is_palindrome("racecar"))      # Output: True
print(count_vowels(my_string))       # Output: 3
print(remove_duplicates("aabbccddeeff")) # Output: abcdef
print(capitalize_words(my_string))    # Output: Hello World!

# Example with case-insensitive palindrome check
print(is_palindrome("Racecar", case_insensitive=True)) # Output: True

# Example of finding a substring
print(find_substring("This is a test string", "test")) # Output: 10 (index of "test")
