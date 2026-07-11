def reverse_arr_1(arr):

    n = len(arr)

    for i in range(n//2):
        arr[i], arr[-i-1]= arr[-i-1], arr[i]
    return arr

# print(reverse_arr_1([1,2,3,4,5,6]))

def reverse_arr_2(arr):
    return arr[::-1]

# print(reverse_arr_2([1,2,3,4,5]))
