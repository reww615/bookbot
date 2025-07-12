from collections import Counter
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_location = {sys.argv[1]}
with open(sys.argv[1]) as f:
    get_book_text = f.read()
#print(get_book_text)  # Print the first 1000 characters of the book text


# Count the number of words and characters in the book text
get_num_words = len(get_book_text.split())
#print(f"{get_num_words} words found in the document")

# Count the number of characters in the book text
get_num_chars = Counter(get_book_text.lower())
char_dict = dict(get_num_chars)
sorted_char_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
