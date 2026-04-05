prompt = "Please enter your age: "

while True:
    ticket = input(prompt)
    ticket = int(ticket)

    if ticket < 3:
        print(f"Since you are the age of {ticket}, your ticket is free.")
        break
    elif ticket < 12:
        print(f"Since you are the age of {ticket}, your ticket is $10.")
        break
    else:
        print(f"Since you are the age of {ticket}, your ticket is $15.")
        break