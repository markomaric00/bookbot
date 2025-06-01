from stats import get_num_of_words, get_num_of_each_char, get_sorted_dict_by_value


def get_book_text(filepath):
    """
    Reads the content of a book from a text file.

    Args:
        filepath (str): The path to the text file containing the book.

    Returns:
        str: The content of the book.
    """
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def main():
    """
    Main function to execute the book reading functionality.
    """
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    try:
        print(
            f"============ BOOKBOT ============\nAnalyzing book found at {filepath}..."
        )
        print("\n----------- Word Count ----------")
        book_text = get_book_text(filepath)
        num_words = get_num_of_words(book_text)
        print(f"Found {num_words} total words")
        char_count = get_num_of_each_char(book_text)
        print("----------- Character Count ----------")
        sorted_char_count = get_sorted_dict_by_value(char_count)
        for char_count in sorted_char_count:
            print(f"{char_count['char']}: {char_count['num']}")
        print("============= END ===============")
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
