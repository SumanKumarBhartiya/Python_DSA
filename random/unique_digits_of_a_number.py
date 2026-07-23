def unique_digits_of_a_number(number):

    str_number = str(number)

    set_number = set(str_number)

    return len(set_number)


print(unique_digits_of_a_number(12345221321010381))