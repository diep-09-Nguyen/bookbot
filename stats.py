def get_book_text(path_to_file):
    
    with open(path_to_file) as book:
        book_contents = book.read()
    
    return book_contents

def get_num_words(path_to_file):

    number_of_words = len(str.split(get_book_text(path_to_file)))

    return number_of_words

def get_num_characters(path_to_file):

    character_count = {}

    book_contents = str.split(get_book_text(path_to_file))

    for word in book_contents:
        for character in word:
            char_key = character.lower()
            
            if char_key not in character_count:
                character_count[char_key] = 1
            else:
                character_count[char_key] += 1

    return character_count

def sort_on(dict):
    return dict["num"]

"""
takes dictionary and outputs a list of dictionaries
input: { key: value }
output: ({"char": "key", "num": "value" })
"""
def dict_to_list(dict_character_count):
    _list_of_dicts = []
    for key in dict_character_count:
        _list_of_dicts.append({"char": key, "num": dict_character_count[key]})
    return _list_of_dicts

"""
prints a sorted list of dictionaries
input: dictionary
output: none
"""
def print_report(dict_character_count):

    _list_to_print = dict_to_list(dict_character_count)
    
    _list_to_print.sort(reverse=True, key=sort_on)
    
    for item in _list_to_print:
        print(f"{item["char"]}: {item["num"]}")