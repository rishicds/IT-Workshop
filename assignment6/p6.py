def order_tuples(tuples, order_list):
    ordered_tuples = []
    for order in order_list:
        for tup in tuples:
            if tup[0] == order:
                ordered_tuples.append(tup)
    return ordered_tuples

tuples = [(1, 'a'), (2, 'b'), (3, 'c')]
order_list = [2, 3, 1]
print(order_tuples(tuples, order_list))
