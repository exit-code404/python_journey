aliens = {
    'alien 0': {'color': 'green', 'points': 5, 'speed': 'slow'},
    'alien 1': {'color': 'yellow', 'points': 10, 'speed': 'medium'},
    'alien 2': {'color': 'red', 'points': 15, 'speed': 'fast'},
    'alien 3': {'color': 'purple', 'points': 20, 'speed': 'extra fast'},
    'alien 4': {'color': 'orange', 'points': 25, 'speed': 'ultra fast'},
    'alien 5': {'color': 'aqua', 'points': 30, 'speed': 'lightning fast'},

}

for alien, value in aliens.items():
    print(alien)

    for stat, key in value.items():
        print(f"\t{stat}: {key}")


