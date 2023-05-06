#Write a Python program to get the Factorial number of given number.

fact=1
n=int(input("Enter number:"))

for i in range(1,n+1):
    fact=fact*i
print("Factorial",n,"is",fact)
