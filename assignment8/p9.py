def split_on_hyphens(str1):
    return str1.split('-')

# Example usage
str1 = "Emma-is-a-data-scientist"
print("\n".join(split_on_hyphens(str1)))
# Output:
# Emma
# is
# a
# data
# scientist
