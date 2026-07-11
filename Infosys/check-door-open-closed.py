def print_status_of_doors(n):
    for i in range(1, n + 1):
        divisors = 0
        for j in range(1, i + 1):
            if i % j == 0:
                divisors += 1
        if divisors % 2 == 0:
            print("closed", end=" ")
        else:
            print("open", end=" ")

n = 5
print_status_of_doors(n)