
from abc import ABC, abstractmethod

# Interface / Abstract Class
class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


# Implementation Class
class Dog(Animal):

    def make_sound(self):
        print("Dog says: Woof Woof!")


# Main Program
dog = Dog()
dog.make_sound()
