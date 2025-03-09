def get_num_words(content):
    num_words = 0
    words = content.split()
    for word in words:
        num_words += 1
    print_num_words = f"Found {num_words} total words"
    return (print_num_words)

def get_num_types(content):
    words = content.lower()
    diff_ch = {}
    for ch in words:
        if ch in diff_ch:
            diff_ch[ch] += 1
        else:
            diff_ch[ch] = 1
    return (diff_ch)

def print_report(print_num_words, diff_ch):

    filtered_counts = {char: count for char, count in diff_ch.items() if char.isalpha()}
    
    print("=========== BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(print_num_words)
    print("--------- Character Count -------")

    sorted_counts = dict(sorted(filtered_counts.items(), key=lambda item: item[1], reverse=True))


    for char, count in sorted_counts.items():
        print(f"{char}: {count}")

    print("============= END ===============")
