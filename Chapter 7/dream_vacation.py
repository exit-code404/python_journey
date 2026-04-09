prompt = "\nWhat location would you like to visit anywhere in the world?"
prompt += "\nPress 'exit' to close the program. "

repeat_prompt = "\nWould you like to add another location to your dream-list? (yes/no) "

vacation = []

active_poll = True
while active_poll:
    location = input(prompt)

    if location.lower() == 'exit':
        active_poll = False
    else:
        vacation.append(location)

        repeat = input(repeat_prompt)

        if repeat.lower() == 'no':
            active_poll = False



print("\n--- Dream Vacation results ---")
for place in vacation:
    print(place.title())            