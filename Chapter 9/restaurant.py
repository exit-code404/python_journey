"""A Class that can be used to represent any restaurant."""
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