# Q. Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# Ans. Find the index of the first non-repeating character in a string or return -1 if none exists.



def firstUniqChar(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1