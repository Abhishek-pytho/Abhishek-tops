#Write a Python program to test whether a passed letter is a vowel or not.



def vowel(x):
 
    if (x == 'a' or x == 'e' or
        x == 'i' or x == 'o' or x == 'u'):
        print("Vowel")
    else:
        print("Consonant")
 
# Driver code
vowel('c')
vowel('e')
