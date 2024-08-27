def sort_by_frequency(tuples):
    # Create a dictionary to count the frequency of the second element
    freq_dict = {}
    for tup in tuples:
        key = tup[1]
        if key in freq_dict:
            freq_dict[key] += 1
        else:
            freq_dict[key] = 1

    # Implement a simple sorting algorithm based on frequency
    for i in range(len(tuples)):
        for j in range(0, len(tuples) - i - 1):
            if freq_dict[tuples[j][1]] < freq_dict[tuples[j+1][1]]:
                tuples[j], tuples[j+1] = tuples[j+1], tuples[j]

    return tuples

# Example usage
tuples = [(1, 3), (2, 2), (3, 3), (4, 2), (5, 1)]
sorted_tuples = sort_by_frequency(tuples)
print(sorted_tuples)
