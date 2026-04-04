prompt = "\nPlease enter the name of the city you have visited:"
prompt += "\n(Enter 'quit' to close the program) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I would love to go to {city.title()}.")