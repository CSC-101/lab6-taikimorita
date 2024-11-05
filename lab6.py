import data
from typing import Optional, List

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_book_from(books: List[data.Book], start: int) -> Optional[int]:
    if start >= len(books) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(books)):
        if books[idx].title < books[mindex].title:
            mindex = idx

    return mindex

# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_book_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp

# Part 1
    """
    Sorts a list of Book objects in place by their titles in alphabetical order.

    Input: 
    - books: A list of Book objects, where each Book has a 'title' attribute.

    Output: 
    - The function modifies the input list of books and does not return a value.

    Data Representation:
    - The data is represented as a list of Book objects, defined in the data module.
    Each Book object contains an attribute 'title' of type str which is used for comparison.
    """
def selection_sort_books(books: List[data.Book]) -> None:
    for idx in range(len(books) - 1):
        mindex = index_smallest_book_from(books, idx)
        if mindex is not None:
            books[idx], books[mindex] = books[mindex], books[idx]

# Part 2
    """
    Swaps the case of each character in the input string.

    Input: 
    - input_str: A string containing characters to be case-swapped.

    Output: 
    - A new string with all lowercase characters converted to uppercase and vice versa.

    Data Representation:
    - The data is represented as a string, which is processed character by character.
    """
def swap_case(input_str: str) -> str:
    result = []
    for char in input_str:
        if char.islower():
            result.append(char.upper())
        elif char.isupper():
            result.append(char.lower())
        else:
            result.append(char)
    return ''.join(result)

# Part 3
"""
    Replaces all occurrences of a specific character in the input string with a new character.

    Input: 
    - input_str: The original string in which replacements will be made.
    - old: The character in the input string to be replaced.
    - new: The character to replace the old character with.

    Output: 
    - A new string with all instances of 'old' replaced by 'new'.

    Data Representation:
    - The data is represented as a string for input, and both the 'old' and 'new' characters are also strings.
    """
def str_translate(input_str: str, old: str, new: str) -> str:
    result = []
    for char in input_str:
        if char == old:
            result.append(new)
        else:
            result.append(char)
    return ''.join(result)

# Part 4
"""
    Creates a histogram (word frequency count) from the input string.

    Input: 
    - input_str: A string containing words separated by spaces.

    Output: 
    - A dictionary where keys are unique words from the input string and values are their respective counts.

    Data Representation:
    - The data is represented as a string (input) which is split into words, and the histogram is returned as a dictionary.
    Each key is a word (string) and the corresponding value is the count (integer) of occurrences of that word.
    """
def histogram(input_str: str) -> dict[str, int]:
    word_counts = {}
    words = input_str.split()

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts
