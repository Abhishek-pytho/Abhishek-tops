"""
 Write a Python program to add 'ing' at the end of a given string (length 
should be at least 3). If the given string already ends with 'ing' then add 
'ly' instead if the string length of the given string is less than 3, leave it 
unchanged.
"""

s = input("Enter the string:")
def add_ing(a):
    if len(a) >= 3 and a[-3:] != "ing":
        a = s + "ing"
        return a
    else:
        print (a + "ly")
print (add_ing(s))
