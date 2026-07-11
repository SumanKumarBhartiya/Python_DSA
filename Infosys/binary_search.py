def binarySearch(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:

        mid = left + (right - left) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            left = mid + 1

        else:
            right = mid - 1

    return -1

arr = [2, 3, 4, 10, 40]
x = 4

result = binarySearch(arr, x)
print(arr, "-----------------")