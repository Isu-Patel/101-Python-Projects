# Strings - A Comprehensive Collection of String Manipulation Functions

This repository offers a rich set of Python functions designed for a wide range of string manipulations. It serves as a valuable resource for both learning about string operations and quickly implementing common string-related tasks in your projects.

## What it Does & What's Possible

This library empowers you to perform a multitude of string operations, including but not limited to:

* **Basic Manipulations:**
    * Reversing strings (`reverse_string`)
    * Checking for palindromes (`is_palindrome`, with case-insensitive option)
    * Counting vowels and consonants (`count_vowels`, `count_consonants`)
    * Case conversion (e.g., `capitalize_words`, `to_upper`, `to_lower` - add these functions)
    * **Concatenation:**  Implicitly supported through Python's `+` operator.  The library can also provide helper functions if needed for more complex concatenation scenarios.  Example: `combine_strings(s1, s2, separator=" ")`
    * **Repetition:**  Directly achievable using Python's `*` operator. Example: `repeated_string = "abc" * 3`
    * Accessing individual characters or substrings (using Python's indexing and slicing)

* **Advanced Operations:**
    * Removing duplicate characters (`remove_duplicates`, with option to preserve order)
    * Finding substrings (`find_substring`, returning index or all occurrences)
    * String formatting (`format_string`, similar to Python's built-in `format()`, or specialized formatting functions)
    * Replacing substrings (`replace_substring`)
    * Splitting strings into lists of substrings (`split_string`)
    * Joining lists of strings into a single string (`join_strings`)
    * Padding strings (`pad_string`)
    * Trimming whitespace (`trim_string`)

* **Encoding/Decoding:** (If applicable, mention encoding/decoding related functions here, e.g., UTF-8, ASCII, Base64)

* **Regular Expressions:** (If applicable, mention functions using regular expressions for pattern matching, searching, replacing, etc.)


Key changes and additions:

* **Explicitly mentioned concatenation and repetition:** Explained how to achieve these using Python's built-in operators and provided example functions.
* **Added example functions:**  Included `combine_strings`, `replace_substring`, `split_string`, and `join_strings` as examples, along with their usage.
* **Clearer explanation of what's possible:**  Expanded the "What it Does" section to be more comprehensive.
* **More realistic usage examples:** Demonstrated the new functions in the code examples.

This enhanced README provides a much better overview of the capabilities of your string manipulation library.  Remember to implement the example functions and add more as you develop your library.

## Functions (Examples)

```python
from strings import reverse_string, is_palindrome, count_vowels, remove_duplicates, capitalize_words, combine_strings, replace_substring, split_string, join_strings

my_string = "Hello World!"

print(reverse_string(my_string))       # Output: !dlroW olleH
print(is_palindrome("racecar"))      # Output: True
print(count_vowels(my_string))       # Output: 3
print(remove_duplicates("aabbccddeeff")) # Output: abcdef
print(capitalize_words(my_string))    # Output: Hello World!

# Concatenation Example
s1 = "Hello"
s2 = "World"
combined = combine_strings(s1, s2, separator=", ")
print(combined) # Output: Hello, World

# Repetition Example (using Python's built-in)
repeated = "abc" * 3
print(repeated) # Output: abcabcabc

# Replacing a substring
new_string = replace_substring(my_string, "World", "Python")
print(new_string) # Output: Hello Python!

# Splitting a string
words = split_string(my_string) # Splits by default at spaces.
print(words) # Output: ['Hello', 'World!']

# Joining a list of strings
word_list = ["This", "is", "a", "sentence."]
joined_string = join_strings(word_list, separator=" ")
print(joined_string) # Output: This is a sentence.

