def union_and_intersection(set1, set2):
    union_set = set1.union(set2)
    intersection_set = set1.intersection(set2)
    return union_set, intersection_set


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union, intersection = union_and_intersection(set1, set2)
print("Union:", union)
print("Intersection:", intersection)
