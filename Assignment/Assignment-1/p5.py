# Write python program that swap two number with temp variable and without temp variable.


#Python program to swap numbers using temporary variable
num1 = int (input ("Enter the first number: "))
num2 = int (input ("Enter the second number: ")) 

#Print original number

print ("First number is : ", num1)
print ("The Second number is : ", num2) 

#Swapping without using temporary variable

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

#Print Swapped number
print ("After swapping") 
print ("First number is : ", num1)
print ("The Second number is : ", num2) 
