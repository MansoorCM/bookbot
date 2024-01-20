def main():
    path = "books/frankenstein.txt"
    text = get_file_text(path)
    print(text)
    print(f"word count is {get_word_count(text)}")
    print(f"letter count is {get_letter_count(text)}")

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

if __name__ == '__main__':
    main()