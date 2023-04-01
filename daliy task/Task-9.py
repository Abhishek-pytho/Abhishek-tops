#WAP swap vlue without using third variable

a=int(input("enter a:"))
b=int(input("enter b:"))

a=a+b
b=a-b
a=a-b

print("updated a:",a)
print("updated b:",b)
