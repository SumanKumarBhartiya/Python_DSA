def max_cons_ones_1(arr):
    max_consecutive = consecutive = 0

    for val in arr:
        if val == 1:
            consecutive += 1
        elif max_consecutive < consecutive:
            max_consecutive = consecutive
            consecutive = 0
        else:
            consecutive = 0
    return max(consecutive, max_consecutive)

# print(max_cons_ones_1([1, 1, 0, 1, 1, 1]))


# difference is time complexity
def max_cons_ones_2(arr):
    consecutive = max_consecutive = 0

    for val in arr:
        if val == 1:
            consecutive += 1
            if max_consecutive < consecutive:
                max_consecutive = consecutive
        else:
            consecutive = 0

    return max_consecutive

# print(max_cons_ones_2([1, 1, 0, 1, 1, 1]))
