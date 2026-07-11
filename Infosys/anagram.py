#  Given two strings s and t, return true if t is an anagram of s, and false otherwise. 
# You may assume the string contains only lowercase alphabets.

def anagram(s,t):

    if len(s)!= len(t):
        return False
    
    char_count = {}
    for ch in s:
        if char_count.get(ch, 0) != 0:
            char_count[ch] = char_count[ch] + 1
        else:
            char_count[ch] = 1
    for ch in t:
        if char_count.get(ch, 0) != 0:
            char_count[ch] = char_count[ch] - 1
        else:
            return False
    if sum(char_count.values()) == 0:
        return True
    return False

print(anagram("anagram", "margana"))
           