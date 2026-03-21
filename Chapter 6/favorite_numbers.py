fav_numb = {
    'daniel': [6, 42, 17, 88],
    'anne': [2, 55, 3],
    'anna': [19, 8, 63, 27],
    'torgeir': [14, 51, 22, 95],
    'rune': [9, 11, 36],
    'herdis': [30, 5, 66, 77, 48],
}

for key in fav_numb:
    print(f"{key.title()}:")
    for value in fav_numb[key]:
        print(f"\t- {value}")