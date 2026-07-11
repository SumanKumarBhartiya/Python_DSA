# Given a number n, return the count of digits in this number.

def digit_count(n):

    return len(str(abs(n)))

def digit_count_2(n):

    n = str(n)

    if n[0] == '-':
        return len(n) - 1
    return len(n)


def digit_count_3(n):

    if n == 0:
        return 1
    
    count = 0

    while n != 0:

        n = n//10
        count += 1
    
    return count