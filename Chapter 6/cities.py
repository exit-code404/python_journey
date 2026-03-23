cities = {
    'rome': {
        'country': 'italia',
        'population': 2750000,
        'fact': 'The Pantheon, built nearly 2,000 years ago, still holds the '
        'record for the worlds largest unreinforced concrete dome'
    },

    'kyoto': {
        'country': 'japan',
        'population': 1500000,
        'fact': 'It was deliberately spared from Allied bombing during WWII, '
        'partly due to its immense cultural and historical significance.'
    },

    'melbourne': {
        'country': 'australia',
        'population': 6000000,
        'fact': 'It has the largest Greek population of any city outside of Greece itself.'
    },
}

for city, value in cities.items():
    print(city.title())

    for key, fact in value.items():
        
        if key == 'country':
            print(f"\t{key.title()}: {fact.title()}")
        else:
            print(f"\t{key.title()}: {fact}")