def fibonacci_numbers(n):
    ans = []
    f1, f2 = 0, 1
    ans.append(f1)

    for i in range(1, n):
        ans.append(f2)
        next = f1 + f2
        f1 = f2
        f2 = next
    return ans


def fibonacci_numbers_2(n):
    if n == 0:
        return []
    
    if n==1:
        return [0]

    ans = [0, 1]

    prev = ans[0]
    curr = ans[1]

    for i in range(2, n):
        head = prev + curr
        ans.append(head)
        prev = curr
        curr = head

    return ans

print(fibonacci_numbers(17))
print(fibonacci_numbers_2(17))