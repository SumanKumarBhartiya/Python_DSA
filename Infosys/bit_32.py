# Python program to find binary 
# representation of a given number

def getBinaryRep(n):
    ans = ""
    
    # Check for each bit.
    for i in range(31, -1, -1):
        
        # If i'th bit is set 
        if (n & (1 << i)):
            ans += '1'
        else:
            ans += '0'
    
    return ans

if __name__ == "__main__":
    n = 2
    print(getBinaryRep(7))