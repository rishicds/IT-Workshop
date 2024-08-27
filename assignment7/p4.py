def remove_duplicates(d):
    seen_values = []
    new_dict = {}
    for key, value in d.items():
        if value not in seen_values:
            seen_values.append(value)
            new_dict[key] = value
    return new_dict

# Example usage
my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3}
print(remove_duplicates(my_dict))
