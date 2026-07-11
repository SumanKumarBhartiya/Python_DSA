# Given an array prices[] of non-negative integers, representing the prices of the 
# stocks on different days, find the maximum profit possible by buying and selling 
# the stocks on different days when at most one transaction is allowed. Here one transaction 
# means 1 buy + 1 Sell. 
# If it is not possible to make a profit then return 0.

def best_time_to_buy_and_sell_stocks(arr):

    maximum = 0

    for i, val in enumerate(arr):
        sub_arr_maximum = max(arr[i:])

        if val < sub_arr_maximum:
            maximum = max(maximum, sub_arr_maximum - val)
        
    return maximum

print(best_time_to_buy_and_sell_stocks([ 7, 8, 9, 10, 11, 5, 6, 4, 3, 2,1]))