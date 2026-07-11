def maximum_sub_array(arr : list):
    
    n = len(arr)
    dp = [0]*n
    dp[0] = arr[0]
    for i in range(1,n):
        dp[i] = max(arr[i], dp[i-1] + arr[i])
    
    return max(dp)


# print(maximum_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


def maximum_sub_array_2(arr):
    if not arr:
        return 0

    current_sum = arr[0]
    max_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum
print(maximum_sub_array_2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))