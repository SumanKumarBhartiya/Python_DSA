def majority_element(arr):
    majority_dict = {}
    for val in arr:
        if val in majority_dict:
            majority_dict[val] +=1
        else:
            majority_dict[val] = 1
    
    for key, count in majority_dict.items():
        if count > len(arr)/2:
            return key

    return None


# print(majority_element([3, 2, 3, 2, 3, 2, 2, 3, 3]))

def majority_element_2(arr):
    majority_dict = {}

    for val in arr:
        majority_dict[val] = majority_dict.get(val, 0) + 1

    for key, count in majority_dict.items():
        if count > len(arr) // 2:
            return key

    return None

print(majority_element_2([3, 2, 3, 2, 3, 2, 2]))