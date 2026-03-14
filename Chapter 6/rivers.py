rivers = {'amazon': 'brazil', 'danube': 'germany', 'yangtze': 'china'}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

for river in rivers.keys():
    print(f"River: {river.title()}")

for country in rivers.values():
    print(f"Country: {country.title()}")

            