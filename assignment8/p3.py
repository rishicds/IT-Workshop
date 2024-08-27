def arrange_string_characters(str1):
    lower_chars = [ch for ch in str1 if ch.islower()]
    upper_chars = [ch for ch in str1 if ch.isupper()]
    return ''.join(lower_chars + upper_chars)

# Example usage
str1 = "PyNaTive"
print(arrange_string_characters(str1))  # Output: yaivePNT
