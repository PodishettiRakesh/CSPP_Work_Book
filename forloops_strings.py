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

def reverseOrder(str):
    revOrder=""
    for i in range(len(str)-1,-1,-1):
        revOrder+=str[i]
    return revOrder
# print(reverseOrder("apple"))



'''Develop a Python program to find and print all occurrences of a given 
substring within a larger string using a for loop to iterate over characters by index.'''
sub="bob"
main="hellobob bobmorley"
def findOccurance(sub,main):
    # count=0
    occur=[]
    n=len(sub)
    for i in range(0,len(main)-n):
        print(main[i:i+n])
        if main[i:i+n]==sub:
            

            occur.append(main[i:i+n])
    return occur
# print(findOccurance(sub,main))


'''Write a Python program to compress a given string by replacing consecutive 
repeated characters with a single character followed by the count of repetition 
using a for loop to iterate over characters by index.'''
def replaceConsecutive(str1):
    
    new=""
    count=1
    for i in range(len(str1)-1):
        
        if str1[i]==str1[i+1]:
            count+=1
        else:
            new+=str1[i]+str(count)
            count=1
    new+=str1[-1]+str(count)
    return new
str12="apple"
# print(replaceConsecutive(str12))


'''Create a Python program to check if one string is a rotation of another 
string. For example, "abcd" is a rotation of "cdab" using a for loop to iterate over characters by index.'''
def is_rotation(str1,str2):
    if len(str1)!=len(str2):
        return False
    for i in range(len(str1)):
        if str1[i:]+str1[0:i]==str2:
            return True
    return False
# print(is_rotation("abcd","cdab"))