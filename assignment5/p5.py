#Write a Python program to find the index of an item in a specified list.

def find_index(list1, item):
    return list1.index(item)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
item = 5
print(find_index(list1, item))