def union_of_arr_with_duplicates_1(arr1 : list, arr2: list) -> int:

    seen = set()

    for val in arr1:
        if val not in seen:
            seen.add(val)
    for val in arr2:
        if val not in seen:
            seen.add(val)

    return len(seen)

# print(union_of_arr_with_duplicates_1([1,2,3,4,5], [1,2,3]))

def union_of_arr_with_duplicates_2(arr1 : list, arr2: list) -> int:

    set1 = set(arr1)
    set2 = set(arr2)

    return len(set1.union(set2))


print(union_of_arr_with_duplicates_2([1,2,3,4,5], [1,2,3]))