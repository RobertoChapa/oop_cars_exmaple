# Parent class
class Car:
    def __init__(self, make, model, engine_type, year):
        self.make           = make
        self.model          = model
        self.engine_type    = engine_type
        self.year           = year

    def describe(self):
        print(f"This vehicle is a {self.year} {self.make} {self.model}.")

    def type_engine(self):
        print("The engine starts quietly.")

# Child class: Sedan
class Sedan(Car):
    def __init__(self, make, model, engine_type, year, seats=5, mpg=30):
        super().__init__(make, model, engine_type, year)
        self.seats = seats
        self.mpg   = mpg

    def type_engine(self):
        print(f"The {self.make} sedan's {self.engine_type} engine starts smoothly and quietly.")

    def sedan_features(self):
        print(f"Seats: {self.seats}, Fuel Economy: {self.mpg} mpg")

# Child class: Truck
class Truck(Car):
    def __init__(self, make, model, engine_type, year, four_wheel_drive=True, towing_capacity=10000):
        super().__init__(make, model, engine_type, year)
        self.four_wheel_drive = four_wheel_drive
        self.towing_capacity = towing_capacity

    def type_engine(self):
        print(f"The {self.make} truck's {self.engine_type} engine rumbles powerfully.")

    def truck_features(self):
        drive = "4-wheel drive" if self.four_wheel_drive else "2-wheel drive"
        print(f"Drive Type: {drive}, Towing Capacity: {self.towing_capacity} lbs")

# Child class: MuscleCar
class MuscleCar(Car):
    def __init__(self, make, model, engine_type, year, horsepower=450, top_speed=180):
        super().__init__(make, model, engine_type, year)
        self.horsepower = horsepower
        self.top_speed = top_speed

    def type_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s {self.engine_type} roars with incredible power!")

    def muscle_car_features(self):
        print(f"Horsepower: {self.horsepower} HP, Top Speed: {self.top_speed} mph")

#--------------------------------------------------------------#

# Creating instances of each subclass
sedan = Sedan("Honda", "Accord", "I4", 2024, seats=5, mpg=33)
truck = Truck("Chevrolet", "Silverado", "V8", 2024, four_wheel_drive=True, towing_capacity=12000)
muscle_car = MuscleCar("Dodge", "Charger", "6.2L Supercharged V8", 2024, horsepower=797, top_speed=203)

# List demonstrating polymorphism
vehicles = [sedan, truck, muscle_car]

# Demonstrate polymorphism clearly
for vehicle in vehicles:
    vehicle.describe()
    vehicle.type_engine()
    
    # Displaying unique features using isinstance for clarity
    if isinstance(vehicle, Sedan):
        vehicle.sedan_features()
    elif isinstance(vehicle, Truck):
        vehicle.truck_features()
    elif isinstance(vehicle, MuscleCar):
        vehicle.muscle_car_features()

    print()  # Blank line for readability












