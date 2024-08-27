def count_chars_digits_symbols(str1):
    chars = digits = symbols = 0
    for ch in str1:
        if ch.isalpha():
            chars += 1
        elif ch.isdigit():
            digits += 1
        else:
            symbols += 1
    return chars, digits, symbols

# Example usage
str1 = "P@#yn26at^i5ve!"
chars, digits, symbols = count_chars_digits_symbols(str1)
print(f"Chars = {chars}, Digits = {digits}, Symbols = {symbols}")
# Output: Chars = 8, Digits = 3, Symbols = 4
