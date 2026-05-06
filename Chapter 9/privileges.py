"""A Class that creates Privileges for Roles."""

class Privileges:
    """Defining the Privileges for the different account roles."""

    def __init__(self, privileges):
        """Initialize the Privileges attribute."""
        self.privileges = privileges

    def show_privileges(self):
        """Print all the active privileges of the admin role."""
        print("Active Privileges:")
        for privilege in self.privileges:
            print(f"\tPrivilege: [{privilege}]")
