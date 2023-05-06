"""
 Write a Python program to count the number of characters (character 
frequency) in a string.
"""


text = "he lpoo llo hhe oo op "
 

chr_f = {}
 
for i in text:
    if i in chr_f:
        chr_f[i] += 1
    else:
        chr_f[i] = 1
 
# printing result
print("Count of all characters : " + str(chr_f))
