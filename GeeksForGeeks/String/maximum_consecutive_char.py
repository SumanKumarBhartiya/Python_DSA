# Python program to find the maximum consecutive
# repeating character in given string

# Function to find out the maximum repeating
# character in given string
def maxRepeating(s):
    n = len(s)
    maxCnt = 0
    res = s[0]

    # Find the maximum repeating character
    # starting from s[i]
    for i in range(n):
        cnt = 0
        for j in range(i, n):
            if s[i] != s[j]:
                break
            cnt += 1

        # Update result if required
        if cnt > maxCnt:
            maxCnt = cnt
            res = s[i]

    return res

s = "aaaabbaaccdeee"
print(maxRepeating(s))

def maxRepeatedChar(s):

    max_cnt = 0
    i = 0
    res = s[i]
    n = len(s)

    while i < n:
        count = 0
        for j in range(i, n):
            if s[i] != s[j]:
                break

            count += 1
        
        if count > max_cnt:
            max_cnt = count
            res = s[i]

        i = j + 1
    
    return res

print(maxRepeatedChar(s))
