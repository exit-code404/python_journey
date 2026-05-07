from random import randint

class Dice:
    """Making a rollable random dice."""

    def __init__(self, sides=6):
        """Giving the Dice an Attribute"""
        self.sides = sides

    def roll_dice(self):
        """Making the dice roll"""
        current_random = randint(1, self.sides)
        print(f"The dice rolled a {current_random}!")

die = Dice(20)

die.roll_dice()

