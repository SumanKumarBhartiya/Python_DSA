def power(x, y):

    i = 0
    while x**i <= y:

        if x**i == y:
            return True
        i += 1
    
    return False


print(power(10, 11))

        
