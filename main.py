from stats import get_num_words
from stats import get_num_characters
from stats import print_report
import sys

def main():

    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print("============ BOOKBOT ============")
    path_to_file = sys.argv[1]
    print(f"Analyzing book found at {path_to_file}...")

    print("----------- Word Count ----------")
    number_of_words = get_num_words(path_to_file)
    print(f"Found {number_of_words} total words")

    print("--------- Character Count -------" )
    character_dict = get_num_characters(path_to_file)
    print_report(character_dict)

main()
