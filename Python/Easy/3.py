def greet():
    print("Hello, world!")

def add(a, b):
    return a + b

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

greet()
print(add(10,20))
car = Car("BMW", "S Class")
print(car.make)
print(car.model)

