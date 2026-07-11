def count_inversions(arr):

    count = 0
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1

    return count


# print(count_inversions([2, 4, 1, 3, 5]))
# print(count_inversions([2, 3, 4, 5, 6]))
print(count_inversions([10,10, 10]))