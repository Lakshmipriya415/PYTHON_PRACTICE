"""
# not applied inheritance
class Baseclass:  
    a=10
    b=100
    def display(self):
        print("Base class")

class DerivedClass:
    c=20
    d=30
    def show(self):
        print("Derived Class")

baseobject=Baseclass()  #base class object
print(baseobject.a, baseobject.b)
baseobject.display()

dobject=DerivedClass()
print(dobject.c,dobject.d)
dobject.show() 
"""

class Baseclass:
    a=10
    b=100
    def display(self):
        print("Base class")

class DerivedClass(Baseclass):    #inheritance applied when it created like this, no need to create 2nd object
    c=20
    d=30
    def show(self):
        print("Derived Class")

baseobject=DerivedClass()  #base class object
print(baseobject.a, baseobject.b, baseobject.c, baseobject.d)
baseobject.display()
baseobject.show()
