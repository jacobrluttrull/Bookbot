from stats import get_num_words, get_num_times_char_appears, sort_on
import sys


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    # read the book text
    book_text = get_book_text(book_path)

    # word count section
    print("----------- Word Count ----------")
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")

    # character count section
    print("--------- Character Count -------")
    char_counts = get_num_times_char_appears(book_text)

    # build list of {"char": x, "count": y} and sort it in place
    char_list = []
    for char, count in char_counts.items():
        if char.isalpha():  # only include letters
            char_list.append({"char": char, "count": count})

    # Boot.dev wants .sort with a sort_on function as the key
    char_list.sort(key=sort_on, reverse=True)

    for item in char_list:
        print(f"{item['char']}: {item['count']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()

