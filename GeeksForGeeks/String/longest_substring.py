def longest_substring(string: str):

    seen = set()

    left = max_len = 0

    for right in range(len(string)):

        while string[right] in seen:

            seen.remove(string[left])
            left +=1
        seen.add(string[right])
        max_len = max(max_len, right - left +1)

    return max_len

print(longest_substring("abcabcacdefghe"))

def longest_substring_2(string: str):

    sub_str = ""
    max_len = 0

    for char in string:
        if char in sub_str:
            index = sub_str.index(char)
            sub_str = sub_str[index+1:] + char
        else:
            sub_str += char
        max_len = max(max_len, len(sub_str))
    
    return max_len

print(longest_substring_2("abcabcacdefghe"))