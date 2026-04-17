def describe_city(city, country="norway"):
    '''Describes a city with its corresponding country.'''
    print(f"{city.title()} is in {country.title()}.")

describe_city(city="tromsø")
describe_city(city="trondheim")
describe_city(city="amsterdam", country="netherlands")    