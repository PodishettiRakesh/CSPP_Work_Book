'''Write a Python function to calculate the factorial of a 
given number n.The factorial of a non-negative 
integer n is the product of all positive integers less than or equal to n.'''
def factorial(n):
    value=1
    for i in range(1,n+1):
        value=value*i
    return value
# print(factorial(5))

def fact(n):
    val=1
    while n>0:
        val=val*n
        n=n-1
    return val
# print(fact(5))


'''
Write a Python function to check if a given string is a palindrome or not.
 A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.
'''
def ispalindrone(word):
    word=str(word)
    if word[::-1]==word:
        return True
    return False
# print(ispalindrone(55755))
# print(ispalindrone("mommom"))

'''Write a Python function that takes a list of numbers as input 
and returns the maximum element in the list.'''
def find_max(lst):
    return max(lst)
# print(find_max([1,2,3,4]))
def findmax(lst):
    big=lst[0]
    for i in lst:
        if i>big:
            big=i
    return big
# print(findmax([1,2,3,4,5]))


'''Write a Python function that takes a string as input and returns the count 
of words in the string. Assume that words are separated by spaces.'''

def countofWords(string):
    words=string.split(" ")
    return len(words)
# print(countofWords("India is my country"))



'''Write a Python function that takes a list as input and returns a 
new list containing the elements of the input list in reverse order.'''
def reverselist(lst):
    # newlst=lst[::-1] 
    # return newlst
    newlst=[]
    count=len(lst)
    for i in range(count-1,-1,-1):
        newlst.append(lst[i])
    return newlst   

# print(reverselist([1,2,3,4,5]))