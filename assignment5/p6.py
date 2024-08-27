#wap in python to find second largest number in a list without inbuilt function

def second_largest_number(list1):
    first = second = -1
    for i in list1:
        if i > first:
            second = first
            first = i
        elif i > second and i != first:
            second = i
    return second

list1 = [10, 20, 4, 45, 99]
print("Second largest number is:", second_largest_number(list1))


