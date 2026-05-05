class Privileges:
    """Defining the Privileges for the different account roles."""

    def __init__(self, privileges):
        """Initialize the Privileges attribute."""
        self.privileges = privileges

    def show_privileges(self):
        """Print all the active privileges of the admin role."""
        print("Active Privilges:")
        for privilege in self.privileges:
            print(f"\tPrivilege: [{privilege}]")

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

class Admin(User):
    """Attempt on making an Administrator"""

    def __init__(self, first_name, last_name, location, field):
        """Initialize the User Attributes and a special Admin Attribute."""
        super().__init__(first_name, last_name, location, field)
        self.privileges = Privileges(['can add post', 'can delete post', 'can ban users'])


user001 = User('Daniel', 'B.', 'Oslo', 'Digital Analyst')
user002 = User('Anna', 'P.', 'Skjetten', 'Lab Researcher')
user003 = User('Emilie', 'W.', 'Lillestrøm', 'Restaurant Waiter')

users = [user001, user002, user003]

for user in users:
    user.greet_user()
    user.describe_user()
    user.privileges.show_privileges()

admin001 = Admin('Rob', 'P.', 'Bergen', 'Digital Administrator')
admin001.describe_user()
admin001.privileges.show_privileges()    