# Given a string s, reverse the string. Reversing a string means rearranging
#  the characters such that the first character becomes the last, 
# the second character becomes second last and so on


def reverse_string(s):
    return s[::-1]


def reverse_str(s):

    output = ""
    for char in s:
        output = char + output
    
    return output


