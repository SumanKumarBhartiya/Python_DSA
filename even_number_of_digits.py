def digits_count(digit, count):
     if digit >=1 and digit <=9:
          return count + 1
     return digits_count(digit//10, count +1)


# print(digits_count(1289, 0))

def even_number_of_digit(arr):
    max_even_digit = 0
    for num in arr:
        count = digits_count(num, 0)
        if count %2 ==0 and max_even_digit < count:
            max_even_digit = count
    return max_even_digit

# print(even_number_of_digit([12, 2, 232, 7896, 3268252, 82735538]))

def even_number_of_digit_2(arr):
    max_even_digit = 0

    for val in arr:
        count = len(str(val))
        if count % 2 == 0 and count > max_even_digit:
            max_even_digit = count
    
    return max_even_digit
# print(even_number_of_digit_2([12, 2, 232, 7896, 3268252, 82735538]))