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

# -----------------------------------------------------------------------------
# Learning Objective: Use string operations and methods to solve problems

'''Write a Python program to check if two given strings are anagrams 
of each other using string operations and methods.'''
def are_anagrams(s1,s2):
    s1=s1.replace(" ","").lower()
    s2=s2.replace(" ","").lower()
    if len(s1)!=len(s2):
        return False
  
    ss1=sorted(s1)
    ss2=sorted(s2)
    # print(ss1,ss2)
    if ss1==ss2:
        return True
    return False    
# print(are_anagrams("rak esh","eshrak"))

def words_freq(sentence):
    words={}
    sentences=sentence.lower().split()
    # print(sentence)
    for word in sentences:
        if word in words:
            print(word)
            words[word]+=1
        else:
            words[word]=1
    return words
# print(words_freq("india is my Country India Is MY country"))



'''Develop a Python program that checks the strength of a given password based on 
certain criteria (e.g., length, presence of uppercase letters, digits, special 
characters) using string operations and methods.'''
# def checkPassword(password):
#     if len(password)>8:
#         if "@" in password:
#             for i in password:
#                 if i.isdigit():
#                     return "strong password"
#             return "password should contain atleast one number"
#         return "@  is missing"
#     return "atleast above 8 chars"
# # print(checkPassword("rakesh"))
# # print(checkPassword("rakesh@"))
# # print(checkPassword("rakesh@123"))
def check_password_strength(password):
    # Criteria for password strength
    min_length = 8
    has_uppercase = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*()-_=+[{]}|;:,<.>/?"
    
    # Check password length
    if len(password) < min_length:
        return "Password is too short. It should be at least 8 characters long."
    
    # Check for uppercase letters, digits, and special characters
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
    
    # Check if all criteria are met
    if has_uppercase and has_digit and has_special:
        return "Password is strong."
    else:
        strength = []
        if not has_uppercase:
            strength.append("uppercase letters")
        if not has_digit:
            strength.append("digits")
        if not has_special:
            strength.append("special characters")
        return "Password is weak. It is missing: " + ", ".join(strength)

# password = input("Enter a password: ")
# print(check_password_strength(password))



'''Write a Python program that validates if a given string is a valid 
email address based on certain rules (e.g., presence of "@" symbol, 
proper domain format) using string operations and methods.'''
def validEmail(email):
    if "@" not in email:
        return False
    first,domain=email.split("@")
    # print(first)
    # print(domain)
    if not first or not domain:
        return False
    if "." not in domain:
        return False
    dom1,dom2=domain.split(".")
    if not dom1 or not dom2:
        return False
    return True
# print(validEmail("rakesh123@gmail.com"))


'''Create a Python program that encrypts and decrypts a given text using a simple 
encryption algorithm (e.g., Caesar cipher) using string operations and methods.
# '''
print(ord("R"))
print(ord("r"))
def encrypt(text):
    cipertext=""
    for each in text:
        if each.isalpha():
            if each.isupper():
                cipertext+=chr((ord(each)-65-2)%26+65)
            else:
                cipertext+=chr((ord(each)-97-2)%26+97)
        else:
            cipertext+=each
    return cipertext
print(encrypt("rakesh"))

