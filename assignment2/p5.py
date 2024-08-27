x,y,z=list(map(int,input("Enter three numbers seperated by spaces ").split()))
print(f"{x} is largest" if x>y and x>z else f"{y} is largest" if y>z and y>x else f"{z} is largest")