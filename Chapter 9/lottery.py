from random import choice

# List containing numbers in chronological order
hovedtall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
             21, 22, 23, 24, 25, 26, 27 , 28, 29, 30,
             31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
             41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

stjernetall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Saving the current winning numbers into a list
current_hovedtall = []
current_stjernetall = []

# The class that the Eurojackpot ticket consist of
class Eurojackpot:
    """Attempt to make a replica of Eurojackpot random drawing."""

    def random_draw_hovedtall(self):
        """Making the random hovedtall"""
        random_hovedtall = choice(hovedtall)
        current_hovedtall.append(random_hovedtall)
        
    def random_draw_stjernetall(self):
        """Making the random stjernetall"""
        random_stjernetall = choice(stjernetall)
        current_stjernetall.append(random_stjernetall)

    def describe_winning_numbers(self):
        """Describes the winning numbers neatly."""
        print("\n--- Winning Numbers ---")
        print(f"Hovedtall: {current_hovedtall}")
        print(f"Stjernetall: {current_stjernetall}")

# Making for loops that uses the Eurojackpot class to create exactly enough numbers

draw = Eurojackpot()

for hoved in range(5):
    draw.random_draw_hovedtall()

for stjerne in range(2):
    draw.random_draw_stjernetall()    

print(draw.describe_winning_numbers())

    

# Known Bugs:
# There is a certain chance of hitting the same number multiple times. This should not be possible.
# There is "None" printed

# Wants:
# I want the numbers to be sorted upon view starting from lowest to highest.