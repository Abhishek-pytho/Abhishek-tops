"""
Write a Python program that will return true if the two given integer 
values are equal or their sum or difference is 5.
"""

def no(x, y):
   if x == y or abs(x-y) == 5 or (x+y) == 5:
       return True
   else:
       return False
print(no(7, 2))
print(no(3, 2))
print(no(2, 2))
print(no(3, 3))
print(no(5, 15))
