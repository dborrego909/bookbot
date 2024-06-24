def main():
    book_path = "books/frankenstein.txt"
    book_text = get_books_text(book_path)
    num_words = get_num_words(book_text)
    print("\n")
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("\n")

    sorted_char_value(get_characters(book_text))
    print("--- End report ---")
    print("\n")

def get_num_words(text):
        words = text.split()
        return len(words)

def get_books_text(path):
        with open(path) as f:
            return f.read()

def get_characters(book_words):
    character_dict = {}
    for char in book_words.lower():
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict

def sorted_char_value(dictionary):
    tuple_list = list(dictionary.items()) #This is creating a list that is a tuple with the characters and then their values.
    sorted_tuple = sorted(tuple_list, key=lambda x: x[1], reverse=True) #This is creating a sorted tuple based on the count. 
    for character, count in sorted_tuple:
        if character.isalpha() == True:
            print(f"The {character} character was found {count} times")


main()
