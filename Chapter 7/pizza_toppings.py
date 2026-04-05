# I wish to create a program that asks about what pizza toppings the user wants,
# by adding it into a visual list that is displayed neatly to the user.

prompt = "\nPlease enter a pizza topping you would like to have on your pizza:"
prompt += "\nPress 'done' to finish the pizza. "

pizza = []

active = True
while active:

    topping = input(prompt)

    if topping == 'done':
        print(f"You pizza has been ordered! You have chosen: {pizza}.")
        active = False
    else:
        pizza.append(topping)
        for toppings in pizza:
            print(toppings)

# Problem 1: This only displays the current item, and not the whole list. SOLVED
# Problem 2: The display is not neat enough. I want it to be formatted into an actual list without the []. SOLVED!