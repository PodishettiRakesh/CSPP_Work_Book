
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
# occurance("jaihanuman jai sri ram)

'''Write a Python program to compress a given string by replacing consecutive 
repeated characters with a single character followed by the count of repetition using slicing operations.'''

def replacing_Consecutive(s):
    if not s:
        return ""
    output = ""
    count = 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            output += s[i] + str(count)
            count = 1

    output += s[-1] + str(count)
        
    return output
# print(replacing_Consecutive("alluarjuuuun"))

'''Create a Python program to check if one string is a rotation of another string.
For example, "abcd" is a rotation of "cdab" using slicing operations.'''

def is_rotation(s1,s2):
    if len(s1)!=len(s2):
        return True
    new=s1*2
    if s2 in new:
        return True
    return False
print(is_rotation("keerthi","thikeer"))