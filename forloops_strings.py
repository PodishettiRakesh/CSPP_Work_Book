'''Write a Python program to check if a given string is a palindrome (reads the same 
forwards and backwards) using a for loop to iterate over characters by index.'''
def ispalindrome(str):
    reversed=""
    for i in range(len(str)-1,-1,-1):
        reversed+=str[i]
    if reversed==str:
        return True
    return False
# print(ispalindrome("rakkdar"))


'''Create a Python program to reverse the order of words in a given sentence
 using a for loop to iterate over characters by index.'''

'''Develop a Python program to find and print all occurrences of a given 
substring within a larger string using a for loop to iterate over characters by index.'''

'''Write a Python program to compress a given string by replacing consecutive 
repeated characters with a single character followed by the count of repetition 
using a for loop to iterate over characters by index.'''

'''Create a Python program to check if one string is a rotation of another 
string. For example, "abcd" is a rotation of "cdab" using a for loop to iterate over characters by index.'''