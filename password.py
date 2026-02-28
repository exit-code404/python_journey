# password strength analyzer
# Input/Output: Can use terminal for now. How can I make the terminal ask
# the user to give input into the terminal for analyzing? 
# Gives feedback based on a set of strong criterias

cons_numbers = ['123', '1234', '12345', '123456', '1234567', '12345678', '123456789', 
                '0123', '01234', '012345', '0123456', '01234567', '012345678', '0123456789']
keyboard_walks = ['qwerty', 'asdfg', 'zxcvb', 'ghjkl', 'yuiop',
                  'ytrewq', 'poiuy', 'gfdsa', 'lkjhg', 'mnbv', 'vcxz']
common_sub = ['p@ssw0rd']

user_input = input("Insert the password for analysis here: ")
print("You entered: " + user_input + " for analysis. Please wait.")

if len(user_input) < 12:
    print("Password needs to have at least 12 characters.")

for value in cons_numbers:
    if user_input == value:
        print("Consecutive numbers is not a strong password!")

for value in keyboard_walks:
    if user_input == value:
        print("Consecutive letters is not a strong password!")

for value in common_sub:
    if user_input == value:
        print("That password is not allowed!")

# I will want a criteria for testing either for atleast
# one uppercase, lowercase, one number, and a special character. I need a proper
# logic for this to work. How will I program a logic that test a pre-written
# sentence of characters if there is one uppercase, one lowercase, one number,
# and one symbol in that sentence?       