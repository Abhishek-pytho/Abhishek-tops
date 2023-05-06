"""Write a Python program to get a single string from two given strings, 
separated by a space and swap the first two characters of each string."""



a=input("Enter a string 1:")

b=input("Enter a string 2:")

x=a[0:2]

a=a.replace(a[0:2],b[0:2])

b=b.replace(b[0:2],x)

print(a,b)
