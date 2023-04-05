a=8
for i in range(0,6):
    for j in range(0,a):
        print(end=" ")
    a=a-2
    for j in range(0,i+1):
        print("* ",end="")
    print()
