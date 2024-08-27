def create_and_add_to_set(elements):
    my_set = set()
    for element in elements:
        my_set.add(element)
    return my_set


elements = [1, 2, 3, 4, 5]
result_set = create_and_add_to_set(elements)
print("Set after adding elements:", result_set)


for item in result_set:
    print(item)
