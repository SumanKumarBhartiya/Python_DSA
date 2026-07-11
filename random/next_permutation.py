def next_permutation(arr):

    n = len(arr)

    for i in range(n-1, 0, -1):
        if arr[i] > arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            return arr

    return arr[::-1]
print(next_permutation([1, 2, 3]))
print(next_permutation([3, 2, 1]))
print(next_permutation([1,1,5]))