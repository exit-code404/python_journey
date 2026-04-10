# Project: Login Simulator
# This program should simulate a simple login system

users = {
    "exitcode": {"password": "password123"},
    "devsec": {"password": "devpass321"},
    "exitsec": {"password": "secure404"},
}

user_prompt = "\nPlease enter your username: "
pass_prompt = "\nPlease enter your password: "

attempts = []

active_login = True
while active_login:
    
    p_username = input(user_prompt)
    
    for user_id in list(users):
     
        if p_username == user_id:
            temp_cache = {}

            print("This username exists")
            temp_cache['username'] = p_username
            cache = temp_cache['username']

            p_password = input(pass_prompt)
            
            length_attempts = len(attempts)
            if length_attempts == 2:
                print("You have been locked out from logging in as you have reached 3 attempts.")
                active_login = False
            elif p_password == users[cache]['password']:
                print("You have successfully logged into the Devsec secure platform.")
            else:
                print("The username exists, but the password is wrong. Try again.")
                attempts += [1]

            break
        
        if p_username not in users:
            print("This username does not exist.")
            repeat = input("Would you like to create a new account? (yes/no) ")

            if repeat.lower() == 'yes':
                create_username = input("Please enter a new username: ")
                create_password = input("Please enter a new password: ")

                new_username = create_username
                new_password = create_password

                users[new_username] = {}
                users[new_username]['password'] = new_password
                print(users)
                user = new_username
                print(f"Creating your new user: {user}")
                
                break
            elif repeat.lower() == 'no':
                active_login = False
            else:
                print("The request entered is not available.")
                break
            continue        


# Bugs:
# Need to access the key:value pairs properly inside the dictionary, and be able to successfully create new accounts. SOLVED
# The new accounts seems to be added to the dictionary correctly, but the program does not recognize the newly created account.SOLVED
# When typing the first username, and doing it again, it does not recognize any other username but the one first entered. SOLVED
# When the break function in the first for loop is done, it sends to the second for loop, even after create account attempt SOLVED

# Needed features:
# Need to add the three attempt feature to locked out. SOLVED
# Need to add 'quit' feature to close the program if needed.
# Rewrite the password checking because no for loop is actually needed here. SOLVED
# Need to add functionality to the 'no' option when creating a new account SOLVED




    



