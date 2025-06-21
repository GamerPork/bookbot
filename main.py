from stats import word_count, character_counts, fancy_report
import sys

if len(sys.argv) != 2:   
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(path) as f:
        readfile = f.read()
    return readfile

def main ():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    book_text = get_book_text(sys.argv[1])
    total_words = word_count(book_text)
    print("Found " f"{total_words} total words")
    char_count = character_counts(book_text)
    print("--------- Character Count -------")
    sorted_chars = fancy_report(char_count)
    for item in sorted_chars:
        char = item["char"]
        count = item["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()
