personal_info_0 = {
    'first name': 'dan',
    'last name': 'johnsen',
    'age': 25,
    'city': 'lillestrøm',
    'work': 'fashion designer',
    'nationality': 'norwegian'
}

personal_info_1 = {
    'first name': 'rune',
    'last name': 'ericson',
    'age': 55,
    'city': 'trondheim',
    'work': 'web developer',
    'nationality': 'norwegian'
}

personal_info_2 = {
    'first name': 'geir',
    'last name': 'olgson',
    'age': 32,
    'city': 'bergen',
    'work': 'banker',
    'nationality': 'english'
}

peoples = [personal_info_0, personal_info_1, personal_info_2]


for people in peoples:
    first_name = f"\nFirst name: {people['first name'].title()}"
    last_name = f"Last name: {people['last name'].title()}"
    age = f"Age: {people['age']}"
    city = f"City: {people['city'].title()}"
    work = f"Work: {people['work'].title()}"
    nationality = f"Nationality: {people['nationality'].title()}"

    personal_info = f"{first_name} \n{last_name} \n{age} \n{city} \n{work} \n{nationality}"

    print(personal_info)
