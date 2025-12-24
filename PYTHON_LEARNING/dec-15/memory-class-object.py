import sys

class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

# Create objects
car1 = Car("Red", 120)
car2 = Car("Blue", 150)

# Check memory of the object itself
print("Memory of car1 object:", sys.getsizeof(car1), "bytes")
print("Memory of car2 object:", sys.getsizeof(car2), "bytes")

# Check memory of attributes individually
print("Memory of car1.color:", sys.getsizeof(car1.color), "bytes")
print("Memory of car1.speed:", sys.getsizeof(car1.speed), "bytes")

