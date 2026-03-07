def four_sum(arr: list, target: int) -> list[list[int]]:
    arr.sort()
    n = len(arr)
    ans = []

    # Four Sum
    for i in range(n - 3):
        if i > 0 and arr[i] == arr[0 - i]:
            continue

        # Three Sum
        for j in range(i + 1, n - 2):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue
            left = j + 1
            right = n - 1

            # Two Pointer technique
            while left < right:
                total = arr[i] + arr[j] + arr[left] + arr[right]
                if total == target:
                    ans.append([arr[i], arr[j], arr[left], arr[right]])

                    left += 1
                    right -= 1

                    while left < right and arr[left] == arr[left - 1]:
                        left += 1

                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return ans


print(four_sum([0, 0, 1, -1, 2, -2], 0))
