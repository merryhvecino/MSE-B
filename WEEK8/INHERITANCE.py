class Vehicle:
    def __init__(self,brand):
        self.brand = 'toyota'
        
    def start(self):
        return f'{self.brand} engine starts'

class Car(Vehicle):
    def start(self):
        return f'{self.brand} car roars to life!'