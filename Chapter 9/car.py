class Car:
    """Simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's kilometers."""
        print(f"This car has {self.odometer_reading} km on it.")

    def update_odometer(self, kilometer):
        """
        Set the odometer to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if kilometer >= self.odometer_reading:
            self.odometer_reading = kilometer
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, km):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += km        


my_new_car = Car('audi', 'rs6', 2026)
my_used_car = Car('merchedes', 'e-class', 2020)

print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(600)
my_new_car.read_odometer() 

print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(50_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()