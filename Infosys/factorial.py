def factorial(n):

    if n==0 or n==1:
        return 1
    elif n > 1:
        return n * factorial(n-1)
    
print(factorial(5))

def factorial_num(n):

    factorial = 1
    while n > 1:

        factorial = factorial * n
        n = n-1
    
    return factorial

print(factorial_num(5))