a = 10
b = 2
c = 1

def greatest(a,b,c):

    if a > b:
        if a > c:
            return a
        else:
            return c
    elif b > c:
        return b
    else:
        return c
    
print(greatest(a,b,c))