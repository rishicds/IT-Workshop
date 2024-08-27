def find_repeated_items(tup):
    seen = []
    repeated = []
    for item in tup:
        if item in seen and item not in repeated:
            repeated.append(item)
        seen.append(item)
    return repeated

tup = (1, 2, 3, 1, 2, 4)
print(find_repeated_items(tup))
