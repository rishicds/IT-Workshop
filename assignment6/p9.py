def sort_by_max_element(tuples):
    for i in range(len(tuples)):
        for j in range(0, len(tuples) - i - 1):
            if max(tuples[j]) < max(tuples[j+1]):
                tuples[j], tuples[j+1] = tuples[j+1], tuples[j]
    return tuples

tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print(sort_by_max_element(tuples))
