def get_book_text(path_to_file):
    
    with open(path_to_file) as book:
        book_contents = book.read()
    
    return book_contents

def get_num_words(path_to_file):

    number_of_words = len(str.split(get_book_text(path_to_file)))

    return number_of_words
