# Given an array of integers, every element in the array appears 
# twice except for one element which appears only once.
#  The task is to identify and return the element that occurs only once

def unique_number(arr):

    unique_sum = sum(set(arr)) # x + y
    arr_sum = sum(arr) # 2x + y

    ans = 2 * unique_sum - arr_sum # 2 * (x + y) - (2x + y)

    return ans

print(unique_number([2, 3, 5, 4, 5, 3, 4, 2, 8]))


# XOR

def findUnique(arr):
    res = 0
    
    # Find XOR of all elements
    for num in arr:
        res ^= num
    
    return res

arr = [ 2, 2, 5, 5, 20, 30, 30 ]
print(findUnique(arr))