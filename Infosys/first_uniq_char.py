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

# def first_unique_char(s):

#     char_list = []

#     for char in s:
#         if char in char_list:
#             char_list.remove(char)
#         char_list.append(char)

#     print(char_list)
#     return char_list[0]

# print(first_unique_char("swisswi"))
        