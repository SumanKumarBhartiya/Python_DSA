def rorate_arr_by_one(arr):
    right = arr.pop()
    return [right] + arr

print(rorate_arr_by_one([1,2,3,4,5]))

