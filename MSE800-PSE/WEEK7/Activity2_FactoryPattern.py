
#Activity Week7-2: Factory Pattern
#Start with reading the code to debug and then explain why the model is following Factory pattern:
 
from abc import ABC, abstractmethod

class Factory(ABC):
   
    @abstractmethod
    def create_product(self, kind=None):
        pass
 
class AnimalFactory(Factory):
    def __init__(self):
        pass
 
    def create_product(self, kind=None):
        if kind == "dog":
            animal = Dog()
        elif kind == "cat":
            animal = Cat()
 
        return animal
 
class DogFactory(Factory):
   
    def create_product(self, kind=None):
        pass
 
class CatFactory(Factory):
   
    def create_product(self, kind=None):
        pass
 
class Animals(ABC):
 
    @abstractmethod
    def run(self):
        pass
 
class Dog(Animals):
 
    def run(self):
        print(f"I'm a Dog, I can run!!")
 
 
class Cat(Animals):
    def __init__(self):
        pass
    
    def run(self):
        print(f"I'm a Cat, I can run!!")
        

factory = AnimalFactory() #Responsible for creating objects
dog = factory.create_product("dog") #method of the factory and passes "dog" as the type.
cat = factory.create_product("cat") #method of the factory and passes ",cat" as the type.
dog.run() #Calls the method of the Dog class
cat.run() #Calls the method of the Cat class
