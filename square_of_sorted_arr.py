def square_of_sorted_arr(arr):
    sq_arr = [ i **2 for i in arr]
    return sorted(sq_arr)

# print(square_of_sorted_arr([-4, -1, 0, 3, 10]))

def square_of_sorted_arr_2(arr):

    n= len(arr)
    ans = [0] * n
    left = 0
    right = n-1
    write_idx = n-1

    while left <= right:

        if abs(arr[left]) >  abs(arr[right]):
            ans[write_idx] = arr[left] **2
            left+=1
        else:
            ans[write_idx] = arr[right] ** 2
            right-=1
        
        write_idx-=1
    
    return ans

print(square_of_sorted_arr_2([-4, -1, 0, 3, 10]))