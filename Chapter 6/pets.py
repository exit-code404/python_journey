axolotl = {
    'pet_name': 'axolotl',
    'species': 'fish',
    'age': 3,
    'weight': '50g',
    'color': 'pink',
    'sex': 'female',
    'location': 'mexico'

}

fennec_fox = {
    'pet_name': 'fennec fox',
    'species': 'fox',
    'age': 6,
    'weight': '1100g',
    'color': 'orange/white',
    'sex': 'male',
    'location': 'north america'

}

sugar_glider = {
    'pet_name': 'sugar glider',
    'species': 'petaurus breviceps',
    'age': 5,
    'weight': '140g',
    'color': 'blue-gray',
    'sex': 'male',
    'location': 'australia'

}

capybara = {
    'pet_name': 'capybara',
    'species': 'rodent',
    'age': 7,
    'weight': '5500g',
    'color': 'brown',
    'sex': 'female',
    'location': 'chile'

}

serval = {
    'pet_name': 'serval',
    'species': 'cat',
    'age': 2,
    'weight': '600g',
    'color': 'yellow',
    'sex': 'female',
    'location': 'africa'

}

kinkajou = {
    'pet_name': 'kinkajou',
    'species': 'mammal',
    'age': 14,
    'weight': '2400g',
    'color': 'light brown',
    'sex': 'male',
    'location': 'mexico'

}

savannah_monitor = {
    'pet_name': 'savannah monitor',
    'species': 'lizard',
    'age': 8,
    'weight': '3600g',
    'color': 'gray',
    'sex': 'female',
    'location': 'afirca'

}

pets = [axolotl, fennec_fox, sugar_glider, capybara, serval, kinkajou, savannah_monitor]

for pet in pets:
    pet_name = f"\nPet Name: {pet['pet_name'].title()}"
    species = f"Species: {pet['species'].title()}"
    age = f"Age: {pet['age']}"
    weight = f"Weight: {pet['weight']}"
    color = f"Color: {pet['color'].title()}"
    sex = f"Sex: {pet['sex'].title()}"
    location = f"Location: {pet['location'].title()}"

    pet_info = f"{pet_name} \n{species} \n{age} \n{weight} \n{color} \n{sex} \n{location}"
    print(pet_info)