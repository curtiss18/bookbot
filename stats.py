def count_words(text):
    num_words = text.split()
    return len(num_words)

def count_characters(text):
    letters_count = {}
    for char in text:
        char_lower = char.lower()
        if char_lower in letters_count:
            letters_count[char_lower] += 1
        else:
            letters_count[char_lower] = 1
    return letters_count

def sort_char(letters_count):
    char_list = []
    for char in letters_count:
        if char.isalpha():
            char_entry = {}
            char_entry["char"] = char
            char_entry["count"] = letters_count[char]
            char_list.append(char_entry)

    def sort_on(char):
        return char["count"]

    char_list.sort(reverse=True, key=sort_on)
    return char_list
