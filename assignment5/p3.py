#wap to print number in list after removing even number from it

def remove_even(lst):
    for i in lst:
        if i%2 != 0:
            print(i)

lst = [1,2,3,4,5,6,7,8,9,10]
remove_even(lst)
