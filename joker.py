# A real Norsk Tipping Joker Simulation

from random import choices, randint

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

class Joker():
    """A simulation of Joker"""
        
    def generate_numbers(self):
        """Generates five random digits from 0 - 9 using random.choices()"""
        return choices(numbers, k=5)
    
    def compare_one_row(self, ticket_number, winning_number):
        """Compares each Winning Number in each Ticket Number row using positional comparison."""
        matches = 0

        for ticket_digit, winning_digit in zip(ticket_number, winning_number):
            if ticket_digit == winning_digit:
                matches += 1

        return matches                    


    def describe_status(self, attempts, joker_candidate_wed, joker_candidate_sat, tier_five_wed, tier_five_sat, tier_four_wed, tier_four_sat, 
                        tier_three_wed, tier_three_sat, tier_two_wed, tier_two_sat, joker_candidate_total, tier_five_total, tier_four_total, 
                        tier_three_total, tier_two_total, price_estimate_wed, price_estimate_sat, price_estimate_total, cost_estimate, net):
        """Describes each tier number of times matched."""
        prompt_wed = "\n--- TIER DRAWN (WEDNESDAY) ---"
        prompt_wed += f"\nJoker-Candidate: {joker_candidate_wed}"
        prompt_wed += f"\nTier 5: {tier_five_wed}"
        prompt_wed += f"\nTier 4: {tier_four_wed}"
        prompt_wed += f"\nTier 3: {tier_three_wed}"
        prompt_wed += f"\nTier 2: {tier_two_wed}"
        prompt_sat = "\n--- TIER DRAWN (SATURDAY) ---"
        prompt_sat += f"\nJoker-Candidate: {joker_candidate_sat}"
        prompt_sat += f"\nTier 5: {tier_five_sat}"
        prompt_sat += f"\nTier 4: {tier_four_sat}"
        prompt_sat += f"\nTier 3: {tier_three_sat}"
        prompt_sat += f"\nTier 2: {tier_two_sat}"
        prompt_total = "\n--- TIER DRAWN (TOTAL) ---"
        prompt_total += f"\nJoker-Candidate: {joker_candidate_total}"
        prompt_total += f"\nTier 5: {tier_five_total}"
        prompt_total += f"\nTier 4: {tier_four_total}"
        prompt_total += f"\nTier 3: {tier_three_total}"
        prompt_total += f"\nTier 2: {tier_two_total}"
        prompt_total += f"\nTotal Estimated Winnings: {price_estimate_total} NOK"
        prompt_total += f"\nTotal Estimated Cost: {cost_estimate} NOK"
        prompt_total += f"\nNet Profit/loss: {net}"
        prompt_total += f"\nTotal Attempts: {attempts}"
        print(prompt_wed)
        print(prompt_sat)
        print(prompt_total)           

# test_joker = Joker()
# print(test_joker.compare_one_row([1, 2, 3, 4, 5], [1, 9, 3, 9, 9]))        

active = True
while active:
    joker = Joker()
    ticket_numbers = []
    attempts = 0
    cost_estimate = 0

    # Wednesday Variables
    joker_candidate_wed = 0
    tier_five_wed = 0
    tier_four_wed = 0
    tier_three_wed = 0
    tier_two_wed = 0 
    price_estimate_wed = 0
      

    # Saturday Variables
    joker_candidate_sat = 0
    tier_five_sat = 0
    tier_four_sat = 0
    tier_three_sat = 0
    tier_two_sat = 0
    price_estimate_sat = 0
    

    # Retrieve the PN and Rows
    pn = input("Please enter your last five digits of your player number: ")
    rows = input("Choose how many rows (One row = 25 NOK): ")
    
    # We want the additional rows to be one less the player has chosen because we want the PN to be the first.
    additional_rows = int(rows) - 1

    # Add the Player Number to the front of the Ticket Numbers list
    player_number = [int(digit) for digit in pn]
    ticket_numbers.append(player_number)    

    # Generate the number of random number rows as the player wanted, and save each row into Ticket Numbers.
    for row in range(additional_rows):
        chosen_number = joker.generate_numbers()
        ticket_numbers.append(chosen_number)

    # Create the draw
    for attempt in range(1_000_000):
        winning_number = joker.generate_numbers()
        attempts = attempts + 1
        cost_estimate += int(rows) * 25

        # Joker Candidate
        if attempt % 2 == 0:
            joker_draw = randint(1, 300000)
            if joker_draw == 1:
                joker_candidate_wed += 1
                price_estimate_wed += 1561700
        else:
            joker_draw = randint(1, 550000)
            if joker_draw == 1:
                joker_candidate_sat += 1
                price_estimate_sat += 2645100

        for ticket_row in ticket_numbers:
            matches = joker.compare_one_row(ticket_row, winning_number)
            is_wednesday = attempt % 2 == 0

            # Add the largest winning tier first, otherwise move on to the next until there is no more.
            if matches == 5:
                if is_wednesday:
                    tier_five_wed += 1
                    price_estimate_wed += 127059
                else:
                    tier_five_sat += 1
                    price_estimate_sat += 136934    
            elif matches == 4:
                if is_wednesday:
                    tier_four_wed += 1
                    price_estimate_wed += 2426
                else:
                    tier_four_sat += 1
                    price_estimate_sat += 2343
            elif matches == 3:
                if is_wednesday:
                    tier_three_wed += 1
                    price_estimate_wed += 179
                else:
                    tier_three_sat += 1
                    price_estimate_sat += 173
            elif matches == 2:
                if is_wednesday:
                    tier_two_wed += 1
                    price_estimate_wed += 30
                else:
                    tier_two_sat += 1
                    price_estimate_sat += 30
            
    # Total Variables
    joker_candidate_total = joker_candidate_wed + joker_candidate_sat
    tier_five_total = tier_five_wed + tier_five_sat
    tier_four_total = tier_four_wed + tier_four_sat
    tier_three_total = tier_three_wed + tier_three_sat
    tier_two_total = tier_two_wed + tier_two_sat
    price_estimate_total = price_estimate_wed + price_estimate_sat
    net = price_estimate_total - cost_estimate

    joker.describe_status(attempts, joker_candidate_wed, joker_candidate_sat, tier_five_wed, tier_five_sat, tier_four_wed, tier_four_sat, 
                        tier_three_wed, tier_three_sat, tier_two_wed, tier_two_sat, joker_candidate_total, tier_five_total, tier_four_total,
                        tier_three_total, tier_two_total, price_estimate_wed, price_estimate_sat, price_estimate_total, cost_estimate, net)
    active = False

       

    
    


    






# Bugs:
# - The matches found are not reset cleanly between iterations making the matched found exceed five. - FIXED
# - The while loop continues making the describe_status() not appearing, and the program not exiting. - FIXED
# - The Joker Candidate never happens because it tries to compare integers with list

# Wants:
# - Add Main game with it's own logic and tiered prices
#   - Draw Logic: One Draw = One attempt on Wednesday (1:300,000) and One attempt on Saturday (1:550,000) - ADDED
#   - Use Choices() function from random to draw random numbers for the additional rows. - ADDED
#   - Match: Iterate through each Index to use positional comparison - ADDED
#       - Compare one row at a time - ADDED
#       - Return matches for that row - ADDED
#       - Count tiers per row, not whole ticket. - ADDED
# - Add a paralell separate draw inside each attempt that is completly random 
#       with chance ranging from 1:300,000 to 1:550,000 - ADDED
#   - Draw Logic: Always drawn from the player-number which is the first row. - ADDED
#       The winning chance is static no matter how many rows inside the main game. - ADDED
# - Add a starting point where we choose how many rows we want to play with and the cost of that. Keep the agreed logic. - ADDED
#   - Choose the player-number to model from the real player-number - ADDED
#   - Choose how many rows. This will decide how many numbers needs to be compared on every draw 
#       and allow to model the costs the draw. - ADDED
# - Simulate the cost versus winnings. - ADDED
#   - Add a note that explains the actual winnings will vary drastically to reality, and it's only an approximation. 
#   - Cost: 25 NOK per row, per day (50 NOK per row, per draw). - ADDED
#   - Winnings: Find the Historical mean per tier and use as constants - ADDED
#       - 2 Match (Wed/Sat): 30 NOK
#       - 3 Match (Wed/Sat): 179 NOK / 173 NOK
#       - 4 Match (Wed/Sat): 2426 NOK / 2343 NOK
#       - 5 Match (Wed/Sat): 127,059 NOK / 136,934 NOK 
#       - Joker-Candidate (Wed/Sat): 1,561,700 NOK / 2,645,100 NOK
# - Add so that the Joker Candidate is directly comparing iself with the player number rather than be pure probabalistic.