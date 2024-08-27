def middle_three_chars(str1):
    if len(str1) % 2 == 0 or len(str1) < 3:
        return "The string length must be odd and greater than or equal to 3."
    mid_index = len(str1) // 2
    return str1[mid_index-1:mid_index+2]

# Example usage
str1 = "JhonDipPeta"
print(middle_three_chars(str1))  # Output: Dip
