def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    dict_char = get_count_characters(text) 
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()

    dict_list = to_list_dict(dict_char)
    
    for item in dict_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
        
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)

    
def get_count_characters(text):
    lowered_text = text.lower()
    num_characters = {}
    for char in lowered_text:
        if char in num_characters:
            num_characters[char] += 1
        else:
            num_characters[char] = 1
    return num_characters


def to_list_dict(dict_char):
    dict_list = [{'char': k, 'num': v} for k, v in dict_char.items()]
    dict_list.sort(key=lambda x: x['num'], reverse=True)
    return dict_list


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
    
main()
