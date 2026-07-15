# Program to print Sum Triangle for a given array

# Given an array arr[], construct its Sum Triangle as follows:

# The bottom row of the triangle is the original array.
# Each element in the row above is formed by adding the two adjacent elements directly below it.
# Continue this process until only one element remains at the top of the triangle.
# Return all elements of the Sum Triangle in top-to-bottom order, and within each row from left to right.

def triangle_sum(arr):

    result = [ arr ]

    output = []
    sub_arr = arr
    while len(sub_arr) > 1:
        n = len(sub_arr)
        for i in range(1, n):
            sum = sub_arr[i-1] + sub_arr[i]
            output.append(sum)

        sub_arr = output
        output = []
        result.append(sub_arr)

    result = result[::-1]
    output = []
    for arr in result:
        output.extend(arr)

    return output

print(triangle_sum([4, 7, 3, 6, 7]))



def getTriangle(arr):
    n = len(arr)
    triangle = [[] for _ in range(n)]

    # Last row contains the original array.
    triangle[n - 1] = arr[:]

    # Build triangle from bottom to top.
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            triangle[i].append(triangle[i + 1][j] + triangle[i + 1][j + 1])

    ans = []

    # Store rows from top to bottom.
    for row in triangle:
        ans.extend(row)

    return ans

# TODO : Do it using recursion

