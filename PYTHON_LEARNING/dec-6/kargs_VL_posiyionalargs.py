"""
def student_info(**kwargs):
    print(kwargs)

student_info(name="Priya", age=25, course="Python")
"""


def create_profile(**kwargs):
    print("User Profile:")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

create_profile(name="Harshini", city="Hyderabad", role="Tester")

