
'''Write a Python program to check if a given string is a palindrome (reads the same forwards and backwards) 
using slicing operations.'''
def checkPalindrome(s):
    if s==s[::-1]:
        return True
    return False
# print(checkPalindrome("uhhgghhyu"))

'''Create a Python program to reverse the order of words in a given sentence using slicing operations.'''
def reverseOrder(s):
    return s[::-1]
# print(reverseOrder("rakesh"))