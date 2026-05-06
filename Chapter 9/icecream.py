from restaurant import Restaurant

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
