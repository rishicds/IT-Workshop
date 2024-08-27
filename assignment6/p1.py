def element_wise_sum(tuples):
    result = []
    for i in range(len(tuples[0])):
        sum_element = 0
        for tup in tuples:
            sum_element += tup[i]
        result.append(sum_element)
    return tuple(result)

tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print(element_wise_sum(tuples))
