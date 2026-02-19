def negative_num_to_end_1(arr):
    data = []
    data_neg = []
    for num in arr:
        if num < 0:
            data_neg.append(num)
        else:
            data.append(num)
    return data + data_neg

# print(negative_num_to_end_1([1, -1, -3, 2, -7, -5, 11, 6]))

def negative_num_to_end_2(arr: list):
    for i , num in enumerate(arr):
        if num < 0:
            arr.remove(num)
            arr.append(num)
    return arr


# print(negative_num_to_end_1([1, -1, -1, 2, -7, -5, 11, 6]))