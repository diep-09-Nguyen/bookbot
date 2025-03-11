from stats import get_num_words

def main():
    number_of_words = get_num_words("books/frankenstein.txt")
    print(f"{number_of_words} words found in the document")

main()
