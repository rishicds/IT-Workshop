def sort_by_frequency(tuples):
    freq_dict = {}
    for tup in tuples:
        if tup[1] not in freq_dict:
            freq_dict[tup[1]] = 1
        else:
            freq_dict[tup[1]] += 1

    for i in range(len(tuples)):
        for j in range(0, len(tuples) - i - 1):
            if freq_dict[tuples[j][1]] < freq_dict[tuples[j+1][1]]:
                tuples[j], tuples[j+1] = tuples[j+1], tuples[j]
    return tuples

tuples = [(1, 3), (2, 2), (3, 3), (4, 2), (5, 1)]
print(sort_by_frequency(tuples))
