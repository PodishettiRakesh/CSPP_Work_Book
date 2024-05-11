
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

'''Develop a Python program to find and print all occurrences of a given substring 
within a larger string using slicing operations.'''

def occurance(long,sub):
    # n=len(sub)
    count=0
    for i in range(0,len(long)-3):
        if long[i]+long[i+1]+long[i+2]==sub:
            count+=1
    #         print(sub)
    # print(count)
# occurance("jaihanuman jai sr