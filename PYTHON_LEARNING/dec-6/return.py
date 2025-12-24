"""
def multiply(a,b):
    c=a*b
    print(c)
    return c                     # if not use the print(x) is none  


x=multiply(3,5)
print(x)
x=2
print(x)
"""

"""
def sum_of_squares(n):
    total=0
    for i in range(1,n+1):
        even=2*i
        total=total+(even*even)    #sum of sqaures of first n even numbers
    return total
print(sum_of_squares(5))
"""


"""
def sum_of_square_odd(n):
    total=0
    for i in range(1,n):
        odd=i
        total=total+(odd*odd)     #sum of sqaures of first n odd numbers
    return total
print(sum_of_square_odd(4))
"""


"""
def printstring(str="priya", number=2):     #number is default argument
    print(str, number)

printstring("Lakshmi")     #str Lakshmi is normal argument 
"""


"""
def student(name, course="Python", duration="3 months"):
    print(name, course, duration)

student("Priya")
student("Anu", "Java",0)    #positional arguments
"""




def student(name, course="Python", duration="3 months"):
    print(name, course, duration)

student("Lakshmi","JAVA","4 months")  #positional arguments

student(name="priya" ,duration="2 months", course="c")   #keyword arguments

student("Harshini")    #default arguments

student("Harish", duration="4")

























