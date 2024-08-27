def sort_lists_in_tuple(tuples):
    sorted_tuples = []
    for tup in tuples:
        sorted_list = []
        for i in range(len(tup)):
            min_val = tup[i]
            min_index = i
            for j in range(i+1, len(tup)):
                if tup[j] < min_val:
                    min_val = tup[j]
                    min_index = j
            tup[i], tup[min_index] = tup[min_index], tup[i]
            sorted_list.append(tup[i])
        sorted_tuples.append(tuple(sorted_list))
    return tuple(sorted_tuples)

tuples = ([3, 2, 1], [6, 5, 4])
print(sort_lists_in_tuple(tuples))
