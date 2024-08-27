#wap in python to get largest number from list

def largest_number(lst):
    max = lst[0]
    for i in lst:
        if i > max:
            max = i
    return max

def main():
    lst = [1,2,3,4,5]
    print(f"Largest number from list is {largest_number(lst)}")