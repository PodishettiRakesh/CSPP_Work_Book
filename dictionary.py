# dic={}
# print(dic)

# dic={"ap":2,"ban":3,"che":5}
# print(dic["ban"])
# for key,val in dic.items():
#     print(key,val)
# print("ban" in dic)

'''Write a function that takes a list of words as input and returns 
a dictionary where the keys are the unique words in the list, and the
values are the frequencies of those words.'''

def create_dict(lst):
    dic={}
    for i in lst:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    return dic
# print(create_dict(["india","america","rakesh","keerthi","keerthi","kavya","india"]))