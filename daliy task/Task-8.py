#WAP take three number from user find the large number using nested .


a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))

if(a>b):
    if(a>c):
        print("a is large")
    else:
        print("c is large")
else:
    if(b>a):
        if(b>c):
            print("b is large")
        else:
            print("c is large")
    else:
        print("a is big")
