def remove_duplicates(input_list):
    return list(set(input_list))


sample_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(sample_list)
print("List after removing duplicates:", unique_list)
