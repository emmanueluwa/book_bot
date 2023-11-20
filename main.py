def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    num_of_words = get_num_of_words(text)
    print(f"{num_of_words} words found in document")
    get_char_count(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_of_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    lower_case_text = text.lower()

    char_count = {}
    for char in lower_case_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

main()