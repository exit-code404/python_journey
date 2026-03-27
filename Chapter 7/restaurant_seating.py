seating = input("Let's find you a table. How many people should the table fit?")
seating = int(seating)

if seating > 8:
    print(f"You have chosen a table for {seating}.")
    print("Please wait while I check for an available table that matches your group...")
    print("I am sorry to announce but we currently do not have any available table at this moment.")
    print("Please wait...")
else:
    print(f"Your table is ready at the second floor with the table number AA23.")