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