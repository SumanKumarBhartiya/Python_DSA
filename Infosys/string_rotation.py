# Check if a string can be obtained by rotating another string 2 places

def string_rotation(str1, str2):

    if len(str1) != len(str2):
        return False
    
    if len(str1) <= 2:
        return str1 == str2
    
    clock_rot = ""
    anticlock_rot = ""
    
    # Store the anti-clockwise rotation of str2
    # by concatenating the last 2 characters to the beginning.
    anticlock_rot = str2[-2:] + str2[:-2]

    # Store the clockwise rotation of str2 by concatenating
    # the first 2 characters to the end.
    clock_rot = str2[2:] + str2[:2]

    # Check if either the clockwise or anti-clockwise 
    # rotation of str2 is equal to str1, and return 
    # the result.
    return str1 == clock_rot or str1 == anticlock_rot