"""class toys:
    doll="barbie"
    ball_colour="white"

access=toys()   #object is access , toys is classname

print(access.doll)
print(access.doll, access.ball_colour)"""



"""class toys:
    doll="barbie"
    ball_colour="white"
    print(doll, ball_colour)  #here in class have direct access variables
    def walk(self):
        print("****************Walking****************")
    def run(self):
        print("***********running****************")

access=toys()   #object is access , toys is classname
print(access.doll, access.ball_colour)  #in object not access class variable direct, use . operator 


access.walk()   #no need to ut self here in brackets, bydefault it call 
access.run()"""


"""class Human():
    #colour="white"  these 2 variable are used for priya and pooj but we can't change colour and height it takes same for both of them , so we use constructor here 
    #height=5
    def __init__(self,colour,height):
        self.colour=colour
        self.height=height
        print(self.colour, self.height)

priya= Human("fair", 5)  #once object is created first constructor will call and exxecute 
pooj= Human("fair", 5.5)
Bhargav=Human("fair",6.5)

print(priya.colour,priya.height)
print(pooj.colour, pooj.height)
print(Bhargav.colour, Bhargav.height)"""



"""class Human():    #CLASS
    def __init__(self):   #CONSTRUCTOR
        print("constructor")   #once object is created first constructor will call and execute

pooj=Human()   #OBJECT1
priya=Human()  #OBJECT2
"""


class Human:
    def __init__(self,c,h):
        self.c=c
        self.h=h
        print(self.c,self.h)
    def run(self,n):
        print(n, "running")
    def walk(self,w):
        print(w, "walking")

priya=Human("fair", 5)
pooj=Human("fair",5.5)

priya.run("priya")
pooj.walk("pooj")




