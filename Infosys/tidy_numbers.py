# Given a number, the task is to check if it is tidy or not.
#  A tidy number is a number whose digits are in non-decreasing order.

def tidy_number(num):

    string = str(num)

    for i in range(1, len(string)):
        if int(string[i-1]) > int(string[i]):
            return False
    
    return True

print(tidy_number(12743))


"""
prev = 10
    
    # Traverse all digits from right to
    # left and check if any digit is
    # smaller than previous.
    while (num):
        rem = num % 10
        num /= 10
        if rem > prev:
            return False
        prev = rem
    return True
"""