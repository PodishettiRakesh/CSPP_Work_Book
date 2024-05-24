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


'''Create a function that takes a string as input and returns a dictionary where the 
keys are the unique characters in the string, and the values are the frequencies of those characters.'''
def chars_dict(str):
    dic={}
    for i in str:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    return dic
# print(chars_dict("Keerthana"))


'''Write a function that takes two dictionaries as input and returns a new dictionary
 containing the merged key-value pairs from both dictionaries. If a key exists in both 
 dictionaries, the value should be the sum of the values from both dictionaries.'''

def merge_dicts(dic1,dic2):
    for key in dic2:
        if key not in dic1:
            dic1[key]=dic2[key]
        else:
            dic1[key]=dic1[key]+dic2[key]
    return dic1
dic1={'india': 2, 'america': 1, 'rakesh': 1, 'keerthi': 2, 'kavya': 1}
dic2={'india': 2, 'america': 1, "australia":2, "paris":1}
# print(merge_dicts(dic1,dic2))