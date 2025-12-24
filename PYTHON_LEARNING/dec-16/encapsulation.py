"""class Demo:
    a=5   #public
    b=100   #public
    def display(self):
        print("************display")

obj=Demo()
print(obj.a,obj.b)
obj.display()"""


"""
class Demo:  #inside class
    __a=5   
    b=100   
    def display(self):
        print(self.__a)

obj=Demo()  #outside the class 
print(obj.__a,obj.b)
obj.display()

####ERROR####################
"""

class Demo:
    __a = 5        # private variable
    b = 100        # public variable

    def __display(self):   # private method
        print(self.__a)

    def show(self):        # public method
        self.__display()  # calling private method inside class

obj = Demo()
print(obj.b)    #  public variable access
obj.show()      #  public method → private method

