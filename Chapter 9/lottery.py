from random import sample

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

    def describe_match_numbers(self):
        """Prints neatly formatted message when there is match."""
        message = "\n --- A MATCH HAS BEEN FOUND! --- \n"
        message += f"\nNumber of Attempts: {attempts}\n"
        print(message)
        self.describe_ticket_numbers()
        self.describe_winning_numbers()    

    def generate_hovedtall(self):
        """Returns 5 random numbers from Hovedtall."""
        return sample(hovedtall, 5)

    def generate_stjernetall(self):
        """Returns 2 random numbers from Stjernetall."""
        return sample(stjernetall, 2)

    def compare_numbers(self):
        """Comparing Ticket numbers with Winning numbers to see if there is a match."""
        self.match_number = 0

        # Checking Hovedtall
        for number in my_hovedtall:
                if number in current_hovedtall:
                    self.match_number += 1

        # Checking Stjernetall
        for number in my_stjernetall:
                if number in current_stjernetall:
                    self.match_number += 1            

# Making for loops that uses the Eurojackpot class to create exactly enough numbers

active = True
# Program should stay on until quit. User should be able to create as many
# unique draws as the user wants.
    
while active:
    draw = Eurojackpot()
    draw.initial_prompt()
    
    
    max_attempts = 1_000_000
    do_attempts = max_attempts + 1
    # Always have +1 the wanted loop count
    for i in range(do_attempts):    
        
        # Generate numbers
        current_hovedtall = draw.generate_hovedtall()
        current_stjernetall = draw.generate_stjernetall()

        # Check to see if there is a ticket. If not compare Ticket numbers to Winning numbers.
        if ticket == 0:
            draw.describe_numbers()

            save_ticket = input("Do you want to buy this ticket? (yes/no) ")

            if save_ticket == 'yes':
                my_hovedtall.extend(current_hovedtall)
                my_stjernetall.extend(current_stjernetall)
                ticket = 1
            else:
                continue
        else:
            # I need to check every number and compare every number to each other for accurate results.
            # Then add a match number as the decider. If match_number == 7 out of 7 there is a match.
            
            # TEMP: Force an comparision
            # current_hovedtall = list(my_hovedtall)
            # current_stjernetall = list(my_stjernetall)

            draw.compare_numbers()

            if draw.match_number < 7:
                attempts = attempts + 1
                continue
            else:
                draw.describe_match_numbers()
                attempts = 0
                ticket = 0
                my_hovedtall.clear()
                my_stjernetall.clear()
                active = False
                break
    
    # Always have the intended loop count here.
    if attempts >= max_attempts:
        print(f"No match found after {attempts} attempts. Try again in another lifetime!")
        active = False        

    
# Known Bugs:
# There is a certain chance of hitting the same number multiple times. This should not be possible. - FIXED
# There is "None" printed - FIXED
# Numbers is saved, which it should. But it is not cleared. - FIXED
# There is double parenthases around the saved ticket - FIXED
# Does not stop at set range - FIXED
# Compare the Winning Hoved with Ticket Hoved, and Winning Stjerne with Ticket Stjerne to get accurate results - FIXED
# After finding a match, it may still print "No match found..." - FIXED
# The compare_stjerne resets match_number back to 0 with current setup - FIXED
# The double brackets are back once again - FIXED by avoiding extend/append and instead use return
# There seems to be an issue causing the initial prompt to reappear after starting the loop. - FIXED


# Wants:
# I want the numbers to be sorted upon view starting from lowest to highest. - ADDED
# Add an on / off switch with neat visible UI - ADDED
# Function to create new numbers - ADDED
# Add so that user can just press the ENTER key instead of having to write 'ENTER'
# Add function to buy ticket, and save those numbers to my_ticket list - ADDED
# Add automatic loop - ADDED
# Instead of using choice and checking for duplicate numbers, I can use sample instead - ADDED
# Clean up the comparing part - ADDED
# This program is somewhat fragile - not bulletproof - as there is possible to add numbers in a way that generates an error.