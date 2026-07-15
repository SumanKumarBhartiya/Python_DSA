# Given an integer n, denoting the number of cuts that can be made on a pancake, 
# 
# find the maximum number of pieces that can be formed by making n cuts.


"""
1 - 2
2 - 4
3 - 7
4 - 11
5 - 16
6 - 22
"""

def maxCuts(n):
    # Start with one piece
    pieces = 1

    # Simulate each cut
    for i in range(1, n + 1):
        pieces += i

    return pieces


n = 6

print(maxCuts(n))

def max_cuts(n):

    # Apply the Lazy Caterer's formula to find
    # the maximum number of pieces formed.
    res = (n * (n + 1)) // 2 + 1 
    # Sum of all the integers till n Sn = (n * (n+1) // 2) 
    #By keeping in mind that without cut also there will be one pieces
    return res


n = 5
print(max_cuts(n))