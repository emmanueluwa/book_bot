def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    num_of_words = get_num_of_words(text)
    char_count_dict = get_char_count(text)
    chars_sorted_list = get_report_sorted_list(char_count_dict)

    print(f"** Report of {path_to_file} **")
    print(f"{num_of_words} words found in document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        else:
            print(f"The '{item['char']}' character was found {item['num']} times")


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

def sort_on(d):
    return d["num"]

def get_report_sorted_list(num_chars_dict):
    sorted_list = []

    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

main()