def min_and_max_1(arr):
    return min(arr), max(arr)

# print(min_and_max_1([1,4,3,2]))

def min_and_max_2(arr):

    min = max = arr[0]

    for val in arr:
        if val > max:
            max = val
        elif val < min:
            min = val
    
    return min, max

# print(min_and_max_2([1,4,3,2]))
