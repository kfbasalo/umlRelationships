# Component Class
class Engine:
    def start(self):
        print("Engine is starting")

# Main Class
class Car:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()
        print("Car is running")

# Main Program
car = Car()
car.start_car()
