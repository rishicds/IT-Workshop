def find_by_key_element(nested_tuples, key):
    for tup in nested_tuples:
        if tup[0] == key:
            return tup
    return None

nested_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
key = 4
print(find_by_key_element(nested_tuples, key))
