def unique_elements_across_sets(*sets):
    all_elements = set()
    for s in sets:
        all_elements.update(s)
    return all_elements

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}
unique_elements = unique_elements_across_sets(set1, set2, set3)
print("Unique elements across sets:", unique_elements)
