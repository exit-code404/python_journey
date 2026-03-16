favorite_language = {
    'daniel': ['python', 'rust'],
    'emilie': ['c'],
    'noemi': ['rust', 'go'],
    'katya': ['python', 'ruby'],
}

for name, languages in favorite_language.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    elif len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is {languages[0].title()}.")
            
