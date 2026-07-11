def minimize_the_height_II(arr, k):
    arr = sorted(arr)
    min = arr[0]
    max = arr[-1]

    ans = max - min
    if max - min + 2 * k < ans:
        ans = max - min + 2 * k
    elif max - min - 2 * k < ans:
        ans = max - min - 2 * k
    return ans


print(minimize_the_height_II([1, 5, 8, 10], 2))
# print(minimize_the_height_II([3, 9, 12, 16, 20], 3))
