class Car:
    def __init__(self, speed):
        print(speed)
        self.c=speed
        print(self.c)


car1=Car(50)
print(car1.c)
car1.c=car1.c+int("50")
print(car1.c)
