"""A Class that simulates Eurojackpot"""
from pathlib import Path

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
                    match_number = match_number + 1 