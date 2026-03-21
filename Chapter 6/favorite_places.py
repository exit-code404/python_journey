favorite_places = {
    'daniel': ['italia', 'japan', 'australia'],
    'sofia': ['arizona', 'austria', 'ethiopia'],
    'kenji': ['mexico', 'china', 'brazil']
}

for name in favorite_places:
    print(name.title())
    for place in favorite_places[name]:
        print(f"\t- {place.title()}")