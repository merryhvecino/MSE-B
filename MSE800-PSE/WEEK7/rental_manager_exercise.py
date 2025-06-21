class RentalManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RentalManager, cls).__new__(cls)
            cls._instance.cars_available = ["Toyota", "Honda", "Ford"]
        return cls._instance

    def rent_car(self, car_name):
        if car_name in self.cars_available:
            self.cars_available.remove(car_name)
            print(f"{car_name} has been rented.")
        else:
            print(f"{car_name} is not available.")

    def show_available_cars(self):
        print("Available cars:", self.cars_available)


manager1 = RentalManager()
manager2 = RentalManager()

manager1.rent_car("Honda")
manager2.show_available_cars()

print("Are both managers the same object?", manager1 is manager2)
print(f"manager1 id: {id(manager1)} and manager2 {id(manager2)}")
