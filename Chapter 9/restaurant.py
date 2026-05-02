class Restaurant:
    """A class capable of handling a restaurant's name and cuisine."""

    def __init__(self, name, cuisine):
        """Initialize the restaurant name and cuisine"""
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """Prints the attributes in order to describe the restaurant."""
        print(f"{self.name} is a {self.cuisine}-styled restaurant.")

    def open_restaurant(self):
        """Prints a message that indicate that the restaurant is open."""
        print(f"{self.name} is now open!")

first = Restaurant('NY Feels', 'Italian')
second = Restaurant('Asian World', 'Asian')
third = Restaurant('Persia', 'Persian')

first.describe_restaurant()
first.open_restaurant()

second.describe_restaurant()
third.describe_restaurant()