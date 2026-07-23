# Given an array prices[] of non-negative integers, representing the prices of the 
# stocks on different days, return the maximum profit possible by buying and selling 
# the stocks on different days when at most one transaction is allowed. 
# Here one transaction means 1 buy + 1 Sell. 
# If it is not possible to make a profit then return 0.

def best_time_to_buy_and_sell_stocks(stocks):

    profit = 0

    for i, val in enumerate(stocks):

        buy = val

        for sell in stocks[i+1:]:

            if profit < sell - buy:

                profit = sell - buy
    return profit

stocks1 = [1, 3, 6, 9, 11]
stocks2 = [7, 10, 1, 3, 6, 9, 2]
print(best_time_to_buy_and_sell_stocks(stocks1))

def best_time_to_buy_and_sell_stocks(stocks):

    profit = 0

    for i, val in enumerate(stocks):

        for sell in stocks[i+1:]:

            profit = max(profit, sell - val)
    return profit
print(best_time_to_buy_and_sell_stocks(stocks1))

def best_time_to_buy_and_sell_stocks(stocks):

    minSoFar = stocks[0]
    profit = 0

    for val in stocks:
        minSoFar = min(minSoFar, val)

        profit = max(profit, val - minSoFar)
    return profit
print(best_time_to_buy_and_sell_stocks(stocks1))