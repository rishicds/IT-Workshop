def join_sets(*sets):
    result_set = set()
    for s in sets:
        result_set.update(s)
    return result_set


set1 = {1, 2, 3}
set2 = {4, 5}
set3 = {6, 7, 8}
joined_set = join_sets(set1, set2, set3)
print("Joined set:", joined_set)
