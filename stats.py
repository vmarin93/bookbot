def count_words_in_book(book):
    words = book.split()
    return len(words)


def count_chars_in_book(book):
    char_count_dict = {}
    for char in book:
        if char.lower() in char_count_dict:
            char_count_dict[char.lower()] += 1
        else:
            char_count_dict[char.lower()] = 1
    return char_count_dict


def sort_on(items):
    return items["num"]


def create_list_of_dicts(char_count_dict):
    dict_list = []
    for key in char_count_dict:
        if key.isalpha():
            new_dict = {"char": key, "num": char_count_dict[key]}
            dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
