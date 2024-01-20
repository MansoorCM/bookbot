def main():
    path = "books/frankenstein.txt"
    text = get_file_text(path)
    word_count = get_word_count(text)
    chars = get_letter_count(text)
    print_report(chars, word_count, path)

def get_file_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    return len(text.split())

def get_letter_count(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered not in chars:
            chars[lowered] = 1
        else:
            chars[lowered] += 1
    return chars

def print_report(chars, word_count, path):
    letters = []
    for char in chars:
        if char.isalpha():
            letters.append([chars[char], char])
    letters.sort(reverse = True)
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print()
    for count, char in letters:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")


if __name__ == '__main__':
    main()