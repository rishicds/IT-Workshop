for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

#b
for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end="")
    print()

#c
for i in range(1, 6):
    for j in range(1, i + 1):
        print("1" if j % 2 == 1 else "0", end="")
    print()
    
num = 1
for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
    
for i in range(1, 6):
    for j in range(1, i + 1):
        print("1" if (i + j) % 2 == 0 else "0", end="")
    print()
    

