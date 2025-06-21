#Activity W8-4: single inheritance in python
#Write a Python program using single inheritance.
#Create two classes: Animal (parent class) and Dog (child class).
#Add a simple method in each class to demonstrate how single inheritance works.
#After writing the code, briefly explain how it works.
#Finally, share your code and explanation here.

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f"{self.name} is eating {food}")
    
    def make_sound(self):
        pass

class Dog(Animal):
    # This is a method override.
    def make_sound(self):
        print(f"{self.name} says woof!")

class Fish(Animal):
    def make_sound(self):
        print(f"{self.name} says blub blub!")
    
    def swim(self):
        print(f"{self.name} is swimming!")

class Snake(Animal):
    def make_sound(self):
        print(f"{self.name} says hiss!")
    
    def slither(self):
        print(f"{self.name} is slithering!")

# Example usage
dog = Dog("Buddy")
dog.make_sound()


