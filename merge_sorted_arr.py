def merge_sorted_arr(arr1, m, arr2, n):

    ret_list = []
    arr_1_ptr = 0
    arr_2_ptr = 0

    while arr_1_ptr < m and arr_2_ptr < n:

        arr_1_val = arr1[arr_1_ptr]
        arr_2_val = arr2[arr_2_ptr]

        if arr_1_val < arr_2_val:
            ret_list.append(arr_1_val)
            arr_1_ptr +=1
        # elif arr_1_val > arr_2_val:
        else:
            ret_list.append(arr_2_val)
            arr_2_ptr +=1
        # elif arr_1_val == arr_2_val:
        #     ret_list.append(arr_1_val)
        #     ret_list.append(arr_2_val)
        #     arr_1_ptr +=1
        #     arr_2_ptr +=1

    while arr_1_ptr <  m:
        ret_list.append(arr1[arr_1_ptr])
        arr_1_ptr+=1
    while arr_2_ptr <  n:
        ret_list.append(arr2[arr_2_ptr])
        arr_2_ptr+=1

    return ret_list

print(merge_sorted_arr([1,2,3,0,0,0],3, [2,5,6], 3))