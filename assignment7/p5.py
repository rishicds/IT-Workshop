def lists_to_dict(keys, values):
    return {keys[i]: values[i] for i in range(len(keys))}

# Example usage
keys = ['a', 'b', 'c']
values = [1, 2, 3]
print(lists_to_dict(keys, values))
