
def num_words(book_string):
    word_list = book_string.split()
    word_count = 0
    for word in word_list:
        word_count += 1
    return word_count

def char_count_dict(book_string):
    char_dict = {}
    word_list = book_string.split()
    
    for words in word_list:
         for char in words:
             if char.lower() in char_dict and char.isalpha() == True:
                 char_dict[char.lower()] += 1
             elif char.lower() not in char_dict and char.isalpha() == True:
                 char_dict[char.lower()] = 1
             else:
                pass
    return char_dict
