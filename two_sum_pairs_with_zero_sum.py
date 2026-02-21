def two_sum_pairs_with_zero_sum(arr):

    seen = set()
    ans = []

    for val in arr:
        rem = 0-val
        if rem in seen:
            ans.append([rem, val])
        else:
            seen.add(val)
    
    return ans


# print(two_sum_pairs_with_zero_sum([-1, 0, 1, 2, -1,-4]))
print(two_sum_pairs_with_zero_sum([6, 1, 8, 0, 4, -9, -1, -10, -6, -5]))