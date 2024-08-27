def count_occurrences_ignore_case(str1, substring):
    str1_lower = str1.lower()
    substring_lower = substring.lower()
    return str1_lower.count(substring_lower)

# Example usage
str1 = "Welcome to INDIA. INDIA is awesome"
substring = "INDIA"
count = count_occurrences_ignore_case(str1, substring)
print(f"The {substring} count is: {count}")  # Output: The INDIA count is: 2
