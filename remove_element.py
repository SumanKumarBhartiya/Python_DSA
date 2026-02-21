def remove_element_1(arr, k):
    while k in arr:
        arr.remove(k)
    return len(arr)

# print(remove_element_1([3, 2, 2, 3], 3))
# print(remove_element_1([0,1,2,2,3,0,4,2], 2))

def remove_element_2(arr, k):
    ptr = 0

    for val in arr:
        if val != k:
            arr[ptr] = val
            ptr+=1

    return ptr

print(remove_element_2([3, 2, 2, 3], 3))
print(remove_element_2([0,1,2,2,3,0,4,2], 2))