from privileges import Privileges
"""A Class representing a User with Privileges."""

class User:
    """Honest attempt to make clean User Information Summary Class"""

    def __init__(self, first_name, last_name, location, field):
        """Initializing all of the attributes necessary to make a simple User Information Summary."""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.field = field
        self.privileges = Privileges(['can add post'])

    def describe_user(self):
        """The actual summary printed of the User"""
        print(f"\n--- User ({self.first_name}) Profile Summary ---")
        print(f"First Name: {self.first_name}") 
        print(f"Last Name: {self.last_name}")
        print(f"Location: {self.location}")
        print(f"Field: {self.field}")

    def greet_user(self):
        """Greets the User."""
        print(f"\nWelcome, {self.first_name} {self.last_name}!")