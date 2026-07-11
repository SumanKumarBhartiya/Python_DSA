def alternate_positive_negative_1(arr):
    positive_nums = []
    negative_nums = []

    for val in arr:
        if val >= 0:
            positive_nums.append(val)
        else:
            negative_nums.append(val)

    arr_ptr = neg_ptr = pos_ptr = 0

    while neg_ptr < len(negative_nums) and pos_ptr < len(positive_nums):

        arr[arr_ptr] = positive_nums[pos_ptr]
        arr_ptr+=1
        pos_ptr+=1
        arr[arr_ptr] = negative_nums[neg_ptr]
        arr_ptr+=1
        neg_ptr+=1
    
    for i in range(pos_ptr, len(positive_nums)):
        arr[i] = positive_nums[i]
    for i in range(neg_ptr, len(negative_nums)):
        arr[i] = negative_nums[i]

    return arr

print(alternate_positive_negative_1([9,4,-2,-1,5,0,-5,-3, 2]))