"""
class Student:
    def __init__(self):
        self.name = "Ravi"
        self.name = "Ravi"

        print(self.name)

s1 = Student()
print(s1.name)
"""




"""
class Motorbike:
    def __init__(self,speed):
        print(speed)
s1=Motorbike(40)
s2=Motorbike(20)
"""


class Motorbike:
    def __init__(self,speed):
        ##to store speeed in an instance or object attribute using self

        self.speed=speed
s1=Motorbike(40)
s2=Motorbike(20)
print(s1.speed)
print(s2.speed)
