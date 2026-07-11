def sortString(s):
    freq = [0] * 26

    for ch in s:

        freq[ord(ch) - ord('a')] += 1

    ans = ""
    for i, val in enumerate(freq):
        if val > 0:
            ans += (chr(i + ord('a'))*val)
    
    return ans

print(sortString("bbcbacaa"))