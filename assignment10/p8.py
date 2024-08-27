def slice_frozenset(fset, start, end):
    fset_list = list(fset)
    return fset_list[start:end]

frozen_set = frozenset([1, 2, 3, 4, 5])
sliced_elements = slice_frozenset(frozen_set, 1, 4)
print("Sliced elements:", sliced_elements)
