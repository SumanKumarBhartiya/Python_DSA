def maximum_sub_array(arr : list):
    
    n = len(arr)
    dp = [0]*n
    dp[0] = arr[0]
    for i in range(1,n-1):
        dp[i] = max(arr[i], dp[i-1] + arr[i])
    
    return max(dp)


print(maximum_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))