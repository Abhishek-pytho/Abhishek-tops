# Write a Python program to count occurrences of a substring in a string



def find_substring(string, substring):
    # Initialize an empty list to store the start indices of the substrings
    indices = []
    # Start searching for the substring from the beginning of the string
    start_index = 0
    # Continue searching until the substring is not found in the remaining part of the string
    while True:
        
        index = string.find(substring, start_index)
        if index == -1:
            # If the substring is not found, break out of the loop
            break
        else:
           
            indices.append(index)
            
            start_index = index + 1
    # Return the list of indices
    return indices
string = "GeeksforGeeks is best for Geeks"
substring = "Geeks"
indices = find_substring(string, substring)
print("The original string is:", string)
print("The substring to find:", substring)
print("The start indices of the substrings are:", indices)
