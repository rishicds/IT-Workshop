#generate all permutations of a list in Python without itertools

def permute(lst, l, r):
    if l == r:
        print(lst)
    else:
        for i in range(l, r+1):
            lst[l], lst[i] = lst[i], lst[l]
            permute(lst, l+1, r)
            lst[l], lst[i] = lst[i], lst[l]

def main():
    lst = [1,2,3]
    print(permute(lst, 0, len(lst)-1))