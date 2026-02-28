players = ['charles', 'martina', 'lawrence', 'mia', 'michael']

print("Here are the players in my team:")
for player in players[:3]:
    print(f"\t- {player.title()}")

print("\nThe first three players in this list are: ")
for player in players[:3]:
    print(f"\t- {player.title()}")

print("\nThe middle three players in the list are: ")
for player in players[1:4]:
    print(f"\t- {player.title()}")

print("\nThe last three players in the list are: ")
for player in players[2:]:
    print(f"\t- {player.title()}")