# Given an array arr[], check if it is sorted in ascending order or not. 
# Equal values are allowed in an array and two consecutive equal values are considered sorted.


def is_sorted(arr : list):

    n = len(arr)

    for i in range(1, n):
        if arr[i-1] > arr[i]:
            return False
    
    return True