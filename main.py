import sys
from stats import get_num_words, get_num_types, print_report
file_contents = ""

def get_book_text(path_of_file):
    global file_contents
    with open(path_of_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    get_book_text(path)
    print_report(get_num_words(file_contents), get_num_types(file_contents))

main()