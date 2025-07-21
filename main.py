import sys
from stats import count_words, count_characters, sort_char

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        return
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    text = get_book_text(path)
    word_count = count_words(text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    character_count = count_characters(text)
    sorted_list = sort_char(character_count)
    print("--------- Character Count -------")
    for char in sorted_list:
        print(f"{char["char"]}: {char["count"]}")
    print("============= END ===============")

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

main()