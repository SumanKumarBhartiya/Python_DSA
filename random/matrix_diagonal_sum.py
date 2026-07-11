def matrix_diagonal_sum(arr):

    left = 0  # 3
    right = len(arr[0]) - 1  # 2
    sum = 0
    for data in arr:
        if left == right:
            sum += data[left]
        else:
            sum = sum + data[left] + data[right]
        left += 1
        right -= 1

    return sum


# print(matrix_diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


# TODO : fix this case as the 1, 2 index have some issues
print(matrix_diagonal_sum([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]))
# print(matrix_diagonal_sum([[5]]))
