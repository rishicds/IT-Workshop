def max_min_dict_values(d):
    values = list(d.values())
    return max(values), min(values)

# Example usage
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(max_min_dict_values(my_dict))
