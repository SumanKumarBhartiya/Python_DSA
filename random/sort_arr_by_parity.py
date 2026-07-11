def sort_arr_by_parity_1(arr):

    even_parity = []
    odd_parity = []

    for val in arr:
        if val % 2 == 0:
            even_parity.append(val)
        else:
            odd_parity.append(val)


    return even_parity + odd_parity

print(sort_arr_by_parity_1([3,1,2,4]))