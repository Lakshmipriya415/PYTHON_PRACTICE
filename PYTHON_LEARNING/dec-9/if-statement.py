"""a=25
print("before starting if")        #if statement
if 0:
    print("After starting if")
"""

"""
even=22
odd=23
if even>=25:
    print("True")        #if-else statement
else:
    print(odd)
"""


"""age = 18

if age > 18:
    print("major")
elif age == 18:             #if-elif-else statement
    print("equal")
else:
    print("minor")
"""

"""
age = 25

if age >= 18:
    print("Adult")

    if age >= 60:
        print("Senior Citizen")
    else:
        print("Not senior")
else:
    print("Minor")
"""


def assign_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    elif marks >= 50:
        return "E"
    else:
        return "F"

print(assign_grade(90))   # A
print(assign_grade(85))   # B
print(assign_grade(73))   # C
print(assign_grade(65))   # D
print(assign_grade(55))   # E
print(assign_grade(40))   # F

