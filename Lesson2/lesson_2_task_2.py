y = 2010

def is_year_leap(y):
    if y % 4 == 0:
        return True
    else:
        return False


x = is_year_leap(y)
print(f"год {y}: {x}")
