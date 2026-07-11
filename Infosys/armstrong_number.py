def armstrong_number(num: int):

    n = len(str(num))

    total = 0
    val = num
    while num > 0:

        rem = num % 10

        num = num // 10

        total += rem**n

    return total == val

print(armstrong_number(123))