def common_divisor_two_number(num1, num2):

    n = min(num1, num2)
    count= 0
    for val in range(1, n + 1):

        if num1 % val == 0 and  num2 % val == 0:
            count += 1
    
    return count


print(common_divisor_two_number(20, 36))