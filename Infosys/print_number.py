def number_print(n):

    if n> 0:
        number_print(n-1)
        print(n, end=" ")
    
number_print(9)