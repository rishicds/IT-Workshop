#wap in python to print sum of all the elements of list

def sum_of_list_elements(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

def main():
    lst = [1,2,3,4,5]
    print(f"Sum of all the elements of list is {sum_of_list_elements(lst)}")