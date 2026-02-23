def merge_intervals(arr):
    if not arr:
        return []

    arr.sort(key=lambda x: x[0])

    merged = [arr[0]]

    for current in arr[1:]:
        prev = merged[-1]

        if current[0] <= prev[1]:
            prev[1] = max(prev[1], current[1])
        else:
            merged.append(current)

    return merged


print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
