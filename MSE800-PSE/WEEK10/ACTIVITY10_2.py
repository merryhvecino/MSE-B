import datetime

cars = {
    "CAR001": {"type": "SUV", "available": True},
    "CAR002": {"type": "Sedan", "available": True},
    "CAR003": {"type": "Hatchback", "available": True}
}

users = ["user1", "user2"]
rentals = {}

def get_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log_action(message):
    with open("rental_log.txt", "a") as log_file:
        log_file.write(f"{get_timestamp()} - {message}\n")

def view_available_cars():
    print("\nAvailable Cars:")
    for car_id, details in cars.items():
        if details["available"]:
            print(f"{car_id} - {details['type']}")
    log_action("Viewed available cars")

def rent_car():
    user_id = input("Enter your user ID: ")
    if user_id not in users:
        print("Invalid user.")
        return

    print("\nAvailable Cars:")
    for car_id, details in cars.items():
        if details["available"]:
            print(f"{car_id} - {details['type']}")
    
    car_id = input("Enter Car ID to rent: ")

    if car_id in cars and cars[car_id]["available"]:
        cars[car_id]["available"] = False
        rentals[user_id] = car_id
        print(f"{user_id} rented {car_id}")
        log_action(f"{user_id} rented {car_id}")
    else:
        print("Car not available or invalid ID.")
        log_action(f"{user_id} failed to rent {car_id}")

def return_car():
    user_id = input("Enter your user ID: ")
    if user_id in rentals:
        car_id = rentals[user_id]
        cars[car_id]["available"] = True
        del rentals[user_id]
        print(f"{user_id} returned {car_id}")
        log_action(f"{user_id} returned {car_id}")
    else:
        print("No rental record found.")
        log_action(f"{user_id} attempted return with no rental")

def car_rental_system():
    while True:
        print("\n--- Car Rental System ---")
        print("1. View Available Cars")
        print("2. Rent a Car")
        print("3. Return a Car")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_available_cars()
        elif choice == "2":
            rent_car()
        elif choice == "3":
            return_car()
        elif choice == "4":
            print("Exiting system.")
            break
        else:
            print("Invalid choice.")
            log_action("Invalid menu choice")
