# Given an array arr[] of n integers and a target value, 
# check if there exists a pair whose sum equals the target.
#  This is a variation of the 2-Sum problem.


def two_sum(arr: list, total : int):

    for i, val in enumerate(arr):
        rem = total - val

        if rem in arr[i+1:]:
            return True
        
    return False

print(two_sum([0, -1, 2, -3, 1], -2))