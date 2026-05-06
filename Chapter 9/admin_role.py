from privileges import Privileges
from user_role import User
"""A Class that represents an Admin role with extra Privileges."""

class Admin(User):
    """Attempt on making an Administrator"""

    def __init__(self, first_name, last_name, location, field):
        """Initialize the User Attributes and a special Admin Attribute."""
        super().__init__(first_name, last_name, location, field)
        self.privileges = Privileges(['can add post', 'can delete post', 'can ban users'])