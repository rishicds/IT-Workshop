def count_items_in_list_dict(d):
    count = 0
    for value in d.values():
        if isinstance(value, list):
            count += len(value)
    return count

# Example usage
my_dict = {'a': [1, 2, 3], 'b': [4, 5], 'c': 6}
print(count_items_in_list_dict(my_dict))
