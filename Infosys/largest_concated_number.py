# Given an array of non-negative integers arr[], arrange them such that their 
# concatenation forms the largest possible number. Return the result as a string,
#  since it may be too large for standard integer types.

from functools import cmp_to_key

def myCompare(s1, s2):
    if s1 + s2 > s2 + s1:
        return -1  
    else:
        return 1

# Function to return the largest concatenated number
def findLargest(arr):
    numbers = [str(ele) for ele in arr]
    
    # Sort the array using the custom comparator
    numbers.sort(key=cmp_to_key(myCompare))

    # Handle the case where all numbers are zero.
    # We are sorting in descending order, so zero 
    # in front means complete array contains zero
    if numbers[0] == "0":
        return "0"

    # Concatenate the sorted array
    res = "".join(numbers)

    return res

arr = [3, 30, 34, 5, 9]
print(findLargest(arr))