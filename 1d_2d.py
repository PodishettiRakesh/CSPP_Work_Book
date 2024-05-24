# ls=[[1,2],[2,3]]
# print(ls[0][1])

# lis=[1,2,3,4,5]
# lis[2]=10
# print(lis)

# lis=[[1,2,3],[4,10,6],[7,8,9]]
# ele=max(max(row) for row in lis)
# print(ele)

'''Write a Python program to add two given matrices (2D lists) and print the result.
'''
def sum_matrices(mat1,mat2):
        if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
             return "matrices cannot be added"
        matrix1=[[1,2,3],[4,5,6],[7,8,9]]
        result = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix1[0])):
                row.append(0)
            result.append(row)
        # print(result)

        for i in range(len(mat1)):
            for j in range(len(mat1[0])):
                result[i][j]+=mat1[i][j]+mat2[i][j]
                # print(result)
        return result

mat1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

mat2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
# print(sum_matrices(mat1,mat2))

'''Create a Python program to find the largest element in a given 1D list and print its value.'''
def findmax(nums):
    result=max((row) for row in nums)
    return result
# print(findmax([1,2,5,8,9,24,12]))

'''Develop a Python program that takes a list of words as input and 
counts the frequency of each word, then prints the word-frequency pairs.'''
def frequency_words(words):
    freq={}
    for word in words:
        if word in freq:
             freq[word]+=1
        else:
             freq[word]=1
    return freq
# print(frequency_words(["raki","mama","kavya","mama","keerthi","raki"]))


'''Write a Python program to find the transpose of a given matrix (2D list) and print the result.'''
def transposeOfMatrix(matrix):
    transposeMatrix=[]
    for i in range(len(matrix)):
        row=[]
        for j  in range(len(matrix[0])):
            row.append(matrix[j][i])
        transposeMatrix.append(row)
    return transposeMatrix

mat1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# print(transposeOfMatrix(mat1))


'''Create a Python program that takes a target value and a 2D list as input, 
then searches for the target value within the list. If found, print its row 
and column indices; otherwise, print "Not found".'''
def findTarget(list,target):
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j]==target:
                return f"row {i+1}  col {j+1}"
    return "target not found in given 2d list"

# print(findTarget([[1,2,3],[4,5,6],[7,8,9,10]],5))

# lis=[1,2,3,1,2,1]
# lis.reverse()
# lis.remove(1)
# lis.reverse()
# print(lis)


      
'''Write a Python program to calculate and print the sum of all elements in a given list.'''
def sumElements(list):
    return sum(list)
# print(sumElements([1,2,3,4]))

'''Create a Python program to reverse the order of elements in a given list and print the reversed list.'''
def reverseElements(lis):
    x=list(reversed(lis))
    return x
# print(reverseElements([1,2,3,4]))

'''Develop a Python program that takes a list as input, removes duplicate elements from the list, and prints 
the modified list without duplicates.'''
def removeduplicates(lst):
    new=[]
    for each in lst:
        if each not in new:
            new.append(each)
    return new
# print(removeduplicates([1,1,2,6,4,3,4]))

'''Write a Python program that takes two sorted lists as input, merges them into a single sorted list, 
and prints the merged list.'''
def mergeSorted(lst1,lst2):
    lst1.extend(lst2)
    new=sorted(lst1)
    return new
# print(mergeSorted([1,3,4,5],[2,4,6,8,10]))

'''Create a Python program that rotates the elements of a given list to the right by a specified number of 
positions and prints the rotated list.'''

def rotateRight(lst,positions):
    rotated=lst[-positions:]+lst[0:-positions]
    return rotated
# print(rotateRight([1,2,3,4],2))

# Immutable datatype in python
'''Immutable Data Types
Immutable data types are those whose values cannot be changed after they are created. If you need to modify an immutable object, you must create a new object with the new value.

Common immutable data types in Python include:

Integers
Floats
Strings
Tuples'''

'''Common mutable data types in Python include:

Lists
Dictionaries
Sets'''


# x=5
# print(x)
# print(id(x))
# x=10
# print(x)
# print(id(x))

# mutable data types 
# tup=(1,2,3,4)
# print(tup.append(7))

# dic={"a":1,"b":2}
# print(dic)

# dic["c"]=3
# print(dic)


# s="hello"
# print(s.append("w"))

# st={1,2,3}
# st.add(4)
# print(st)


# lst=[1,2,3,4,5]
# ele=lst.pop()
# print(lst)
# print(ele)

# def rev(lis):
#     lis.clear()
# lis=[1,2,3,4]
# rev(lis)
# print(lis)


'''find the factorial for the given number'''
def fun(n):
    if n==0:
        return 1
    else:
        return n*fun(n-1)
# print(fun(5))

def fun(n):
    if n<=1:
        return n 
    else:
        return fun(n-1)+fun(n-2)
# print(fun(6))

def fun(n):
    if n>0:
        print(n)
        fun(n-1)
# fun(5)

def fun(n):
    if n==1:
        return 1
    else:
        return n+fun(n-1)
# print(fun(5))

def fun(array,low,high,target):
    # high=len(array-1)
    # low=0
    if high>=low:
        mid=(high+low)//2
        if array[mid]==target:
            return array[mid]
        elif array[mid]>target:
            
            return fun(array,low,mid-1,target)
        else:
            return fun(array,mid+1,high,target)
    else:
        return -1
arr=[2,3,4,10,40]
target=11
# print(fun(arr,0,len(arr)-1,target))

def fun(arr):
    if arr:
        print(arr[-1])
        fun(arr[:-1])
# fun([1,2,3,4])

'''Write a recursive function to calculate the sum of digits of a positive integer.'''
def sumOfDigits(number):
    if number==0:
        return 0
    else:
        return number%10+sumOfDigits(number//10)    
# print(sumOfDigits(12345))


'''Implement a recursive function to compute the factorial of a non-negative integer.'''
def factorilaOfInteger(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorilaOfInteger(n-1)
# print(factorilaOfInteger(4)).


'''Create a recursive function to count the number of digits in a positive integer.'''
def countDigits(n):
    if n==0:
        return 0
    else:
        return 1+countDigits(n//10)  
# print(countDigits(1234))

'''Write a recursive function to find the greatest common divisor (GCD) of two positive integers.'''
def gcd(n1, n2):
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    else:
        return gcd(n2, n1 % n2)
# print(gcd(22,36))


'''Implement a recursive binary search algorithm to find the index of a target element in a sorted list.'''
# def binarySearch(lst,target):
#     # print(lst)
#     low=0
#     # print(low,"low")

#     high=len(lst)-1
#     # print(high,"high")
#     mid=(low+high)//2
#     # print(mid,"mid")

#     if target==lst[mid]:
#         return lst[mid]
#     elif target>lst[mid]:
#         low=mid+1
#         return binarySearch(lst[low:high+1],target)
#     else:
#         high=mid
#         return binarySearch(lst[low:high+1],target)

# print(binarySearch([1,2,3,4,5,10],4))



def binarysearch(lst,target):
    def search(low,high):
        if low>high:
            return -1
        mid=(low+high)//2
        if lst[mid]==target:
            return mid
        elif target>lst[mid]:
            return search(mid+1,high)
        else:
            return search(low,mid-1)
    return search(0,len(lst)-1)
# print(binarysearch([1, 2, 3, 4, 5, 10], 10))  
# print(binarysearch([1, 2, 3, 4, 5, 10], 3))   
# print(binarysearch([1, 2, 3, 4, 5, 10], 6)) 

