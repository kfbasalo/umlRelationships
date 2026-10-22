
# Parent Class
class Animal:
    def eat(self):
        print("Animal is eating")

# Child Class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

# Main Program
dog = Dog()

dog.eat()   # Inherited from Animal
dog.bark()  # Method of Dog
