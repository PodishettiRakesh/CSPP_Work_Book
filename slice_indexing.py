
'''Write a Python program to check if a given string is a palindrome (reads the same forwards and backwards) 
using slicing operations.'''
def checkPalindrome(s):
    if s==s[::-1]:
        return True
    return False
# print(checkPalindrome("uhhgghhyu"))