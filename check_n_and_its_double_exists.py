def check_n_and_its_double_exists_1(arr): # O(n2)

    n = len(arr)

    for i in range(n):

        for j in range(i+1, n):

            if arr[i] == 2 * arr[j] or arr[j] == 2 *arr[i]:
                return True
    
    return False

# print(check_n_and_its_double_exists_1([1, 4, 5, 2, 6, 7]))


def check_n_and_its_double_exists_2(arr): # O(n)

    seen = set()

    for val in arr:

        if val **2 in seen or (val%2 == 0 and val //2 in seen):
            return True
        seen.add(val)
    
    return False

print(check_n_and_its_double_exists_2([1, 4, 5, 2, 6, 7]))