def add_two_numbers(arr1, arr2):

    ans = []
    carry = 0

    for i in range(len(arr1)):

        total = arr1[i] + arr2[i]
        val = total % 10 + carry
        carry = total // 10

        ans.append(val)
    
    if carry != 0:
        ans.append(carry)

    return ans

# half solution, works only if len is same, do for arr1 > arr2 or vice versa

print(add_two_numbers([2, 4, 3], [5, 6, 4]))

