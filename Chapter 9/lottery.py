from random import choice

# List containing numbers in chronological order
hovedtall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
             21, 22, 23, 24, 25, 26, 27 , 28, 29, 30,
             31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
             41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

stjernetall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Saving the current ticket numbers into a list
ticket = 0
attempts = 0
my_hovedtall = []
my_stjernetall = []

# The class that the Eurojackpot ticket consist of
class Eurojackpot:
    """Attempt to make a replica of Eurojackpot random drawing."""

    def initial_prompt(self):
        """Describes the program neatly formatted"""
        initial = "\n--- Eurojackpot Number Generator ---\n"
        initial += "\nGenerate as much unique numbers as you want, and"
        initial += "\nhopefully you strike a lucky shot hitting the jackpot."
        initial += "\nPress 'q' at anytime to quit the program."
        print(initial)

    def random_draw_hovedtall(self):
        """Making the random hovedtall"""
        random_hovedtall = choice(hovedtall)
        while random_hovedtall in current_hovedtall:
            random_hovedtall = choice(hovedtall)
        current_hovedtall.append(random_hovedtall)
    
    def random_draw_stjernetall(self):
        """Making the random stjernetall"""
        random_stjernetall = choice(stjernetall)
        while random_stjernetall in current_stjernetall:
            random_stjernetall = choice(stjernetall)
        current_stjernetall.append(random_stjernetall)

    def describe_numbers(self):
        """Describes the numbers neatly."""
        print("\n--- Ticket Numbers ---")
        print(f"Hovedtall: {sorted(current_hovedtall)}")
        print(f"Stjernetall: {sorted(current_stjernetall)}")

    def describe_ticket_numbers(self):
        """Describes the chosen ticket numbers"""
        print("\n--- Ticket Numbers ---")
        print(f"Hovedtall: {sorted(my_hovedtall)}")
        print(f"Stjernetall: {sorted(my_stjernetall)}")        

    def describe_winning_numbers(self):
        """Describes the winning numbers neatly."""
        print("\n--- Winning Numbers ---")
        print(f"Hovedtall: {sorted(current_hovedtall)}")
        print(f"Stjernetall: {sorted(current_stjernetall)}")

    def generate_hovedtall(self):
        """A for loop that generates the Hovedtall."""
        for hoved in range(5):
            draw.random_draw_hovedtall()

    def generate_stjernetall(self):
        """A for loop that generates the Stjernetall."""
        for stjerne in range(2):
            draw.random_draw_stjernetall()

    def compare_numbers(self, match_number):
        """Comparing winning numbers with ticket numbers to see if it's a match."""
        self.match_number = match_number
        for number in ticket_numbers:
                if number in winning_numbers:
                    self.match_number = self.match_number + 1                
           

# Making for loops that uses the Eurojackpot class to create exactly enough numbers

active = True
# Program should stay on until quit. User should be able to create as many
# unique draws as the user wants.
    
while active:
    draw = Eurojackpot()

    # Save current numbers temporarily into the list below
    current_hovedtall = []
    current_stjernetall = []
    
    draw.initial_prompt()

    enter = input("\nType [E] to generate your numbers: ")

    if enter == 'e':
        draw.generate_hovedtall()
        draw.generate_stjernetall()

        draw.describe_numbers()

        if ticket == 0:
            save_ticket = input("Do you want to buy this ticket? (yes/no) ")

            if save_ticket == 'yes':
                my_hovedtall.extend(current_hovedtall)
                my_stjernetall.extend(current_stjernetall)
                ticket = 1
            else:
                continue
        else:
            # Here we would like to print the Winning Numbers & the Ticket numbers for easy comparison.
            draw.describe_winning_numbers()
            draw.describe_ticket_numbers()
            print(attempts)

            # I need to check every number and compare every number to each other for accurate results.
            # Then add a match number as the decider. If match_number == 7 out of 7 there is a match.
            ticket_numbers = my_hovedtall + my_stjernetall
            winning_numbers = current_hovedtall + current_stjernetall
            draw.compare_numbers(0)

            if draw.match_number < 7:
                attempts = attempts + 1
                continue
            else:
                print("There is a match!")
                draw.describe_ticket_numbers
                draw.describe_winning_numbers
                print(attempts)
                attempt = 0
            print(attempts)  
    elif enter == 'q':
        active = False

    
# Known Bugs:
# There is a certain chance of hitting the same number multiple times. This should not be possible. - FIXED
# There is "None" printed - FIXED
# Numbers is saved, which it should. But it is not cleared. - FIXED
# There is double parenthases around the saved ticket

# Wants:
# I want the numbers to be sorted upon view starting from lowest to highest. - ADDED
# Add an on / off switch with neat visible UI - ADDED
# Function to create new numbers - ADDED
# Add so that user can just press the ENTER key instead of having to write 'ENTER'
# Add function to buy ticket, and save those numbers to my_ticket list - ADDED
# When a ticket has been bought. A loop enables that goes through different numbers until it matches with the ticket. 
# Then a winning screen is shown, and how many attempts it had made before the ticket matched with the winning numbers.

# I need to combine the hovedtall and stjernetall to make comparison work, otherwise it would be a problem to?
#. - I could compare both separately.
# It would be way easier to create the lottery machine method if each important part of the program was made of small
# method bits.
# - Should I do this?