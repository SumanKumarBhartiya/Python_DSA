# Check if a Date is Valid or Not

# Given three integers d, m, and y representing a date in the format dd/mm/yyyy, 
# determine whether the date is valid or not. A valid date must lie between 01/01/1800 and 31/12/9999 
# (inclusive) and satisfy the correct number of days for the given month and year.
from datetime import datetime


def check_month_year(mm, yyyy):
    if yyyy < 1800 or yyyy > 9999:

        return False
    if mm < 1 or mm > 12:
        return False
    
    return True

def valid_date(dd, mm, yyyy):

    ans = check_month_year(mm, yyyy)

    if not ans:
        return ans
    
    if dd < 1 or dd > 31:
        return False
    try:
        datetime(yyyy, mm, dd)
        return True
    except Exception:
        return False

print(valid_date(12, 12, 998))
print(valid_date(23, 8, 2003))
print(valid_date(30, 2, 1700))


d = 23
m = 8
y = 2003

ans = True

# Check year, month and day range

ans = check_month_year(m, y)

if not ans:
    pass

elif d < 1 or d > 31:
    ans = False
elif m == 2:

    # Check leap year
    leap = ((y % 4 == 0 and y % 100 != 0) or (y % 400 == 0))

    if leap:
        if d > 29:
            ans = False
    else:
        if d > 28:
            ans = False

elif m == 4 or m == 6 or m == 9 or m == 11:
    if d > 30:
        ans = False

if ans:
    print("true")
else:
    print("false")