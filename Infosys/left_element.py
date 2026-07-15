#
    

def get_left_element(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return None

def left_element(arr):

    while len(arr) > 1:

        arr.remove(max(arr))
        left_element = get_left_element(arr)
        if left_element:
            return left_element
        arr.remove(min(arr))
        left_element = get_left_element(arr)
        if left_element:
            return left_element
    
    return -1

print(left_element([1,5,4,2, 3]))

def lastRemaining(arr, N):
    
    # If single element in array
    if (N == 1):
        return arr[0]

    # Sort the array
    arr.sort()

    # return middle element
    return arr[(N - 1) // 2]

