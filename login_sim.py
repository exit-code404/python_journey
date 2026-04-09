# Project: Login Simulator
# This program should simulate a simple login system

users = {
    "exitcode": "password123",
    "devsec": "devpass321",
    "exitsec": "secure404",
}

user_prompt = "\nPlease enter your username: "
pass_prompt = "\nPlease enter your password: "

attempts = []

active_login = True
while active_login:
    p_username = input(user_prompt)

    if p_username in users:
        p_password = input(pass_prompt)

        print(attempts)
        if p_password == users[p_username]:
            print(f"You are now successfully logged in! Welcome {p_username}.")
        elif p_password == 'quit':
            active_login = False
        else:
            print("The username exists, but the password is incorrect.")
            attempts = attempts + [1]
            print(attempts)
    elif p_username == 'quit':
        active_login = False
    else:
        print("This username is not to be found.")
        create_account = input("Would you like to create an account? (yes/no) ")

        if create_account.lower() == 'yes':
            new_username = input("Please enter a username you would like to use: ")
            new_password = input("Please enter a password you would like to use: ")

            users[new_username] = new_password
        else:
            active_login = False        

    length_attempts = len(attempts)
    if length_attempts == 3:
        active_login = False 




    



