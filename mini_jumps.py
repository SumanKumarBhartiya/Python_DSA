def mini_jumps(arr):

    n = len(arr)

    if n == 0:
        return -1
    
    if arr[0] == 0:
        return -1
    
    left = 0
    right = arr[0]

    jump = 0

    while right < n:
        max_val = max(arr[left:right])
        left = right
        right+= max_val
        jump +=1




    return jump

# print(mini_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
# print(mini_jumps([1, 4, 3, 2, 6, 7]))
print(mini_jumps([0, 10, 20]))

#    left, right,jump, max 
# 1.    0,  1,      1,  1
# 2.    1,  2,      2,  3
# 3.    