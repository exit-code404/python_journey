class User:
    """Honest attempt to make clean User Information Summary Class"""

    def __init__(self, first_name, last_name, location, field):
        """Initializing all of the attributes necessary to make a simple User Information Summary."""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.field = field

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

user001 = User('Daniel', 'B.', 'Oslo', 'Digital Analyst')
user002 = User('Anna', 'P.', 'Skjetten', 'Lab Researcher')
user003 = User('Emilie', 'W.', 'Lillestrøm', 'Restaurant Waiter')

users = [user001, user002, user003]

for user in users:
    user.greet_user()
    user.describe_user()