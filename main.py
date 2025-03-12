from stats import get_num_words
from stats import get_num_characters
from stats import print_report

def main():
    print("============ BOOKBOT ============")
    
    path_to_file = "books/frankenstein.txt"
    print(f"Analyzing book found at {path_to_file}...")

    print("----------- Word Count ----------")
    number_of_words = get_num_words(path_to_file)
    print(f"Found {number_of_words} total words")

    print("--------- Character Count -------" )
    character_dict = get_num_characters(path_to_file)
    print_report(character_dict)

main()
