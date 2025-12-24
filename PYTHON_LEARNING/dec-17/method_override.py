class Parent:
    def tranport(self):
        print("cycle")

class child(Parent):
    def tranport(self):
        print("bike")

c=child()
c.tranport()   #override parent method , child will run
