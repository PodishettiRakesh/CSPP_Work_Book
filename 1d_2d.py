# ls=[[1,2],[2,3]]
# print(ls[0][1])

# lis=[1,2,3,4,5]
# lis[2]=10
# print(lis)

# lis=[[1,2,3],[4,10,6],[7,8,9]]
# ele=max(max(row) for row in lis)
# print(ele)



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


print(sum_matrices(mat1,mat2))




