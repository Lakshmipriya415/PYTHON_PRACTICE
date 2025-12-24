"""class Car:

    def __init__(self, name):
        self.name =name
        print(name)
        print(self.name)
    def colour(self):
        return "red"


car1=Car("royalenfiled")
print(car1.name)

print(car1.colour())
"""



"""
class pythonlife():
    a=3
    print(a)"""



class pylife():
    a=3
    def output(self):
        print(self.a)

p=pylife()
p.output() 

"""Python internally converts this to pylife.output(p)
self = p
self.a → looks for a inside p
Not found → checks class
Finds a = 3
Prints 3
"""

v=pylife()
v.output()

