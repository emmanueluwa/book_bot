def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    num_of_words = get_num_of_words(text)
    print(f"{num_of_words} words found in document")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_of_words(text):
    words = text.split()
    return len(words)


main()