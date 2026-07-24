def product_array(arr):

    res = []
    n = len(arr)

    for i in range(n):

        product = 1

        for j in range(n):

            if i != j:
                product *= arr[j]
        res.append(product)

    return res

arr = [10, 3, 5, 6, 2]
print(product_array(arr))


def product_array(arr):

    zero_count = 0
    product = 1
    idx = -1
    n = len(arr)


    for i, val in enumerate(arr):
        if val == 0:
            zero_count += 1
            idx = i
        else:
            product *= val

    res = [0] * n
    if zero_count == 0:
        res = [ product // val for val in arr]
    elif zero_count == 1:
        res[idx] = product
    
    return res
    
print(product_array(arr))
    

