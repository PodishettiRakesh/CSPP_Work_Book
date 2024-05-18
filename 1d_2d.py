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
print(findmax([1,2,5,8,9,24,12]))

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
print(frequency_words(["raki","mama","kavya","mama","keerthi","raki"]))



