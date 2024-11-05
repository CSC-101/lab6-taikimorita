import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        books = [data.Book(["Author A"], "B Title"), data.Book(["Author B"], "A Title")]
        expected = 1
        actual = lab6.index_smallest_book_from(books, 0)
        self.assertEqual(expected, actual)

    def test_index_smallest_from_2(self):
        books = [data.Book(["Author A"], "B Title"), data.Book(["Author B"], "A Title")]
        expected = 1
        actual = lab6.index_smallest_book_from(books, 0)
        self.assertEqual(expected, actual)

    def test_index_smallest_from_3(self):
        books = [data.Book(["Author A"], "B Title")]
        expected = None
        actual = lab6.index_smallest_book_from(books, 1)
        self.assertEqual(expected, actual)

    def test_index_smallest_from_4(self):
        books = []
        expected = None
        actual = lab6.index_smallest_book_from(books, 0)
        self.assertEqual(expected, actual)

    def test_selection_sort_books_1(self):
        books = [
            data.Book(["F. Scott Fitzgerald"], "The Great Gatsby"),
            data.Book(["Charles Dickens"], "A Tale of Two Cities"),
            data.Book(["Herman Melville"], "Moby Dick")
        ]
        lab6.selection_sort_books(books)
        sorted_titles = [book.title for book in books]
        self.assertEqual(sorted_titles, ["A Tale of Two Cities", "Moby Dick", "The Great Gatsby"], "Test 1 Failed: Sorting books by title")

    def test_selection_sort_books_2(self):
        single_book = [data.Book(["J.K. Rowling"], "Harry Potter and the Sorcerer's Stone")]
        lab6.selection_sort_books(single_book)
        sorted_titles = [book.title for book in single_book]
        self.assertEqual(sorted_titles, ["Harry Potter and the Sorcerer's Stone"], "Test 2 Failed: Sorting a single book list")

    def test_selection_sort_books_3(self):
        empty_list = []
        lab6.selection_sort_books(empty_list)
        self.assertEqual(empty_list, [], "Test 3 Failed: Sorting an empty book list")

    # Part 1
    def test_selection_sort_books_1(self):
        books = [
            data.Book(["F. Scott Fitzgerald"], "The Great Gatsby"),
            data.Book(["Charles Dickens"], "A Tale of Two Cities"),
            data.Book(["Herman Melville"], "Moby Dick")
        ]
        lab6.selection_sort_books(books)
        sorted_titles = [book.title for book in books]
        self.assertEqual(sorted_titles, ["A Tale of Two Cities", "Moby Dick", "The Great Gatsby"],"Test 1 Failed: Sorting books by title")

    def test_selection_sort_books_2(self):
        single_book = [data.Book(["J.K. Rowling"], "Harry Potter and the Sorcerer's Stone")]
        lab6.selection_sort_books(single_book)
        sorted_titles = [book.title for book in single_book]
        self.assertEqual(sorted_titles, ["Harry Potter and the Sorcerer's Stone"],"Test 2 Failed: Sorting a single book list")

    # Part 2
    def test_swap_case_1(self):
        assert lab6.swap_case("Hello World!") == "hELLO wORLD!", "Test 1 Failed: Mixed case with punctuation"

    def test_swap_case_1(self):
        assert lab6.swap_case("Hola Niño!") == "hOLA nIÑO!", "Test 2 Failed: Non-English characters test"

    # Part 3
    def test_str_translate_1(self):
        assert lab6.str_translate('abcdcba', 'a', 'x') == 'xbcdcbx', "Test 1 Failed: Simple replacement test"

    def test_str_translate_2(self):
        assert lab6.str_translate('hello world', 'z', 'y') == 'hello world', "Test 2 Failed: No replacement needed"

    # Part 4
    def test_histogram_1(self):
        assert lab6.histogram("apple banana apple orange") == {'apple': 2, 'banana': 1, 'orange': 1}, "Test 1 Failed: Simple sentence with repetitions"

    def test_histogram_2(self):
        assert lab6.histogram("cat dog mouse") == {'cat': 1, 'dog': 1, 'mouse': 1}, "Test 2 Failed: Unique words test"

if __name__ == '__main__':
    unittest.main()
