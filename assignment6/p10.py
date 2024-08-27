def remove_nested_records(tuples):
    result = []
    for tup in tuples:
        if not isinstance(tup, tuple):
            result.append(tup)
    return tuple(result)

tuples = ((1, 2), 3, (4, 5), 6)
print(remove_nested_records(tuples))
