def get_num_of_words(book_contents: str) -> int:
    return len(book_contents.split())

def find_char_frequency(book_contents: str) -> dict:
    char_frequency = {}
    for char in book_contents:
        char = char.lower()
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    return char_frequency

def sort_frequency_table(frequency_table: dict) -> list[dict]:
    sorted_table = []
    for char in frequency_table:
        char_and_count = {}
        char_and_count["char"] = char
        char_and_count["num"] = frequency_table[char]
        sorted_table.append(char_and_count)
    sorted_table.sort(key=sort_on, reverse=True)
    return sorted_table

def sort_on(dict) -> int:
    return dict["num"]
