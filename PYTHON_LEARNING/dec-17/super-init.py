"""
super().__init__() is a Python command used within a child class's __init__ method (constructor) to call the __init__ method of its parent (superclass)
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person initialized: {self.name}, {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        # Call the parent class's __init__ method
        super().__init__(name, age)
        self.student_id = student_id
        print(f"Student initialized with ID: {self.student_id}")

# Create an instance of the Student class
student1 = Student("Alice", 20, "12345")

