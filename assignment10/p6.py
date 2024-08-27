def is_subset(set1, set2):
    return set1.issubset(set2)

def is_superset(set1, set2):
    return set1.issuperset(set2)


set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print("Set1 is subset of Set2:", is_subset(set1, set2))
print("Set2 is superset of Set1:", is_superset(set2, set1))
