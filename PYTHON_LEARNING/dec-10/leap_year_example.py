def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(leap_year(1900))





"""
def is_right_angled_triangle(side1,side2,side3):
    if (side1<=0) or (side2<=0) or (side3<=0):
        return False


    a=side3**2
    b=side1**2
    c=side2**2
    if a == b + c or b == a + c or c == a + b:

        return True
    else:
        return False
print(is_right_angled_triangle(3,4,5))

"""
