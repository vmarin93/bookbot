import sys

from stats import count_chars_in_book, count_words_in_book, create_list_of_dicts


def get_book_text(path):
    file_contents = ""
    with open(path, "r") as file:
        file_contents = file.read()

    return file_contents


def print_report(book):
    num_of_words = count_words_in_book(book)
    chars_count_dict = count_chars_in_book(book)
    list_of_dicts = create_list_of_dicts(chars_count_dict)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for dict in list_of_dicts:
        print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    print_report(book)


if __name__ == "__main__":
    main()
