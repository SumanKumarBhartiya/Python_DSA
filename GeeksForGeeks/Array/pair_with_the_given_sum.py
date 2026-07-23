# Given an array arr[] of n integers and a target value, 
# check if there exists a pair whose sum equals the target. 
# This is a variation of the 2-Sum problem.

def pair_with_the_given_sum(arr : list, target : int):

    for i, val in enumerate(arr):
        rem = target - val

        if rem in arr[i+1:]:
            return True

    return False

arr = [0, -1, 2, -3, 1]
target = -2

print(pair_with_the_given_sum(arr, target))
arr = [1, -2, 1, 0, 5]
target = 0
print(pair_with_the_given_sum(arr, target))


def two_sum(arr, target):

    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):

            if arr[i] + arr[j] == target:
                return True
    return False

print(two_sum(arr, target))