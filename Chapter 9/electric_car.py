class Car:
    """Simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = 0

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

    def fill_gas_tank(self):
        """Print a statement about the gas tank levels."""
        if self.gas_tank == 0:
            print("You car has no fuel. Fill it.")
        elif self.gas_tank >= 50:
            print("You car has at least half tank available.")
        elif self.gas_tank >= 90:
            print("You car has full tank.")     

class Battery:
    """A simple attempt to model a battery for an eletric car."""

    def __init__(self, battery_size=550):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-KWh battery.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an Electric Car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric cars do not have gas tanks."""
        print("This car does not have a gas tank!")                            

my_eqs = ElectricCar('Merchedes', 'EQS', 2026)
print(my_eqs.get_descriptive_name())
my_eqs.battery.describe_battery()                