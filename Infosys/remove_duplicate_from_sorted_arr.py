def remove_dup(arr: list):


    seen = set()
    output = []

    
    for val in arr:

        if val not in seen:
            seen.add(val)
            output.append(val)

    return output

print(remove_dup([1,1,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4,4]))