favorite_language = {
    'daniel': 'python',
    'emilie': 'c',
    'noemi': 'rust',
    'katya': 'python',
}

friends = ['emilie', 'noemi']
for name in sorted(favorite_language.keys()):
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_language[name].title()
        print(f"\t{name.title()}, I see you love {language}")

if 'dan' not in favorite_language.keys():
    print("\nDan please take the poll!")

print("\nThe following languages have been mentioned in the poll:")
for language in set(favorite_language.values()):
    print(language.title())

advise_poll = ['rune', 'anne', 'lek', 'noemi', 'katya', 'herdis', 'eli', 'anna']
for name in advise_poll:
    if name in favorite_language:
        print(f"Thank you, {name.title()} for taking the poll!")

    if name not in favorite_language:
        print(f"Since you have not taken our poll yet, we strongly advise you to do so {name.title()}.")    
