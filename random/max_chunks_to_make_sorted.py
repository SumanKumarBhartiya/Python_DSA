def max_chunks_to_make_sorted(arr):

    # TODO : revision

    n = len(arr)
    ans = 0
    maxL = [0] * n
    maxL[0] = arr[0]

    # calculate prefix maximum
    for i in range(1, n):
        maxL[i] = max(arr[i], maxL[i - 1])

    # calculate suffix maximum
    minR = [0] * n
    minR[n - 1] = arr[n - 1]

    for i in range(n - 2, -1, -1):
        minR[i] = min(arr[i], minR[i + 1])

    print(maxL)
    print(minR)
    for i in range(n - 1):
        if maxL[i] <= minR[i + 1]:
            ans += 1

    return ans + 1


print(max_chunks_to_make_sorted([5, 4, 3, 2, 1]))
print(max_chunks_to_make_sorted([2, 1, 3, 4, 4]))
