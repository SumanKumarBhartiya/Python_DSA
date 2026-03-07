def candy(arr):

    n = len(arr)
    count = n
    for i in range(1, n):

        if arr[i-1] != arr[i]:
            count += 1

    return count

# print(candy([1,0,2]))
print(candy([1,2,2]))