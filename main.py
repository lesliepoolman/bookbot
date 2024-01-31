def main():
    book = read_book("books/frankenstein.txt")
    generate_char_count_report(count_letters(book), count_words(book))

def count_letters(book):
    letter_count = {}
    for char in book.lower():
        if char in letter_count.keys():
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    return letter_count

def generate_char_count_report(char_count_dict, word_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("")
    sorted_keys = sorted(char_count_dict.keys())
    for key in sorted_keys:
        if key.isalpha():
            print(f"The '{key}' character was found {char_count_dict[key]} times")
    print("--- End report ---")

def count_words(book):
    return len(book.split())

def read_book(path):
    with open(path) as f:
        return f.read()

main()