def square_of_sorted_arr(arr):
    sq_arr = [ i **2 for i in arr]
    return sorted(sq_arr)

print(square_of_sorted_arr([-4, -1, 0, 3, 10]))