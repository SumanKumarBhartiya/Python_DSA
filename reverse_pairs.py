def reverse_pairs(arr):

    count = 0
    n = len(arr)

    for i in range(n):

        for j in range(i+1, n):

            if arr[i] > 2* arr[j]:
                count +=1

    return count


# print(reverse_pairs([1, 3, 2, 3, 1]))
print(reverse_pairs([2, 4, 3, 5, 1]))