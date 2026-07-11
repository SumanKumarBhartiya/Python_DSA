# Q. Given an array of positive numbers, find the minimum sub array whose sum is greater than
#  or equal to a given number ‘S’.
# Ans. Find the smallest length subarray in an array of positive numbers with sum at least S.

# Approach
    # Initialize two pointers (start and end) and a variable to track the current window sum.
    # Expand the end pointer to include elements until the sum is at least S.
    # Once sum exceeds or equals S, try to shrink the window from the start to find the minimum length subarray fulfilling the condition.
    # Update the minimum length whenever a valid subarray is found.
    # Repeat until end pointer traverses the entire array.


def min_subarray_len(s, arr):
    start = 0
    current_sum = 0
    min_length = float('inf')
    for end in range(len(arr)):
        current_sum += arr[end]
        while current_sum >= s:
            min_length = min(min_length, end - start + 1)
            current_sum -= arr[start]
            start += 1
    return 0 if min_length == float('inf') else min_length