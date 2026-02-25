def best_time_to_buy_and_sell_stock(arr):

    max_val = 0
    buy = arr[0]
    for val in arr:
        if val - buy > max_val:
            max_val = val - buy
        if val < buy:
            buy = val

    return max_val

print(best_time_to_buy_and_sell_stock([7,1,5,3,6,4]))