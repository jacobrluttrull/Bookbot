from stats import get_num_words

def get_book_text(book_path):
    pass
def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        book_text = f.read()
        #print(book_text)
        print(get_num_words(book_text))

main()
