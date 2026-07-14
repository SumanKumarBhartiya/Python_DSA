# Find resultant string after concatenating uncommon characters of given strings

def concated_string(str1: str, str2 : str):

    output = ""

    for ch in str1:

        if ch not in str2:
            output += ch
    for ch in str2:

        if ch not in str1:
            output += ch
    
    return output

print(concated_string("aacdb", "gafd"))
print(concated_string("abcs", "cxzca"))

def concatenatedString(s1: str, s2: str) -> str:
    res = ""
    s = set(s2)

    for c in s1:
        if c not in s:
            res += c
        else:
            s.remove(c)

    res += "".join(s)

    return res

s1 = "abcs"
s2 = "cxzca"
print(concatenatedString(s1, s2)) # Output: bsxz