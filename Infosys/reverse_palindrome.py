# Write a program that takes number and gives the resulting palindrome (if one exists). 
# If it took more than 1, 000 iterations (additions) or yield a palindrome that is 
# greater than 4, 294, 967, 295, assume that no palindrome exist for the given number.


def reverse(num: int):

    rev_num = 0

    while num > 0:

        rev_num = rev_num * 10 + num % 10
        num = num//10
    return rev_num


def isPalindrome(num):
    return (reverse(num) == num)


def ReverseandAdd(num):
    rev_num = 0
    while (num <= 4294967295):
        # Reversing the digits of the number
        rev_num = reverse(num)

        # Adding the reversed number 
        # with the original
        num = num + rev_num

        # Checking whether the number 
        # is palindrome or not
        if(isPalindrome(num)):
            print(num)
            break
        else:
            if (num > 4294967295):
                print("No palindrome exist")



ReverseandAdd(159)