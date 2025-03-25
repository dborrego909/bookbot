from stats import char_count_dict
from stats import num_words

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def sort_on(item):
    return item[1]

def main():

    file_contents = get_book_text("./books/frankenstein.txt")
    word_count = num_words(file_contents)
    char_dict = char_count_dict(file_contents)
    sorted_char = sorted(char_dict.items(), key=sort_on, reverse=True)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, count in sorted_char:
        print(f"{char}: {count}")
    print("============= END ===============")



main()

