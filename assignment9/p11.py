def sort_hyphenated_sequence(sequence):
    words = sequence.split('-')
    words.sort()
    return '-'.join(words)

# Example usage
sample_items = "green-red-yellow-black-white"
print(sort_hyphenated_sequence(sample_items))
# Output: black-green-red-white-yellow
