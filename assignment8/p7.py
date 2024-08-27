def count_char_occurrences(str1):
    char_count = {}
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

# Example usage
str1 = "Apple"
print(count_char_occurrences(str1))  # Output: {'A': 1, 'p': 2, 'l': 1, 'e': 1}
