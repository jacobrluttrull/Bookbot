def get_num_words(book_text):
    words = book_text.split()
    return len(words)


def get_num_times_char_appears(book_text):
    lowered_text = book_text.lower()
    char_count = {}
    for char in lowered_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sort_on(item):
    return item["count"]
