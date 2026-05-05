class Restaurant:
    """A class capable of handling a restaurant's name and cuisine."""

    def __init__(self, name, cuisine):
        """Initialize the restaurant name and cuisine"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """Prints the attributes in order to describe the restaurant."""
        print(f"{self.name} is a {self.cuisine}-styled restaurant.")

    def open_restaurant(self):
        """Prints a message that indicate that the restaurant is open."""
        print(f"{self.name} is now open!")

    def set_number_served(self, served):
        """Prints the number of people that have been served."""
        self.number_served = served
        print(f"There have been {served} people served.")

    def increment_number_served(self, served):
        """Increments a number of people served."""
        self.number_served += served

class IceCreamStand(Restaurant):
    """An attempt to model an Ice Cream Stand restaurant"""

    def __init__(self, name, cuisine):
        """Initialize the attributes for the Ice Cream Stand."""
        super().__init__(name, cuisine)
        

    def get_flavors(self):
        """Print a statement showing the different flavors from a list."""
        flavors = ['vanilla', 'chocolate', 'strawberry', 'vanilla milkshake', 'chocolate milkshake']
        
        print("Ice Cream Stand flavors:")
        for flavor in flavors:
            print(f"- {flavor.title()}")            


ice = IceCreamStand('Ice Cream Stand', 'Ice')
ice.get_flavors()






first = Restaurant('NY Feels', 'Italian')
second = Restaurant('Asian World', 'Asian')
third = Restaurant('Persia', 'Persian')

first.describe_restaurant()
first.open_restaurant()
first.set_number_served(52)
first.increment_number_served(5)
print(first.number_served)

second.describe_restaurant()
third.describe_restaurant()