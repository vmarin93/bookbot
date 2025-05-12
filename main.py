import sys
from stats import get_num_of_words, find_char_frequency, sort_frequency_table

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_contents = get_book_text(file_path)
    num_words = get_num_of_words(book_contents)
    char_frequency = find_char_frequency(book_contents)
    sorted_frequency_table = sort_frequency_table(char_frequency)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words") 
    print("--------- Character Count -------")
    for element in sorted_frequency_table:
        if element["char"].isalpha():
            print(f"{element["char"]}: {element["num"]}")
    print("============= END ===============")

def get_book_text(filepath: str) -> str:
    with open(filepath, "r") as file:
        contents = file.read()
    return contents

main()
