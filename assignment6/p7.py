def filter_by_kth_element(tuples, k, value):
    filtered = []
    for tup in tuples:
        if tup[k] == value:
            filtered.append(tup)
    return filtered

tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
k = 1
value = 5
print(filter_by_kth_element(tuples, k, value))
