import sys
import stats



book_location = stats.book_location
num_words = stats.get_num_words
sorted_char_dict = stats.sorted_char_dict

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in sorted_char_dict.items():
        print(f"{char}: {count}")
    print("============= END ===============")

main()