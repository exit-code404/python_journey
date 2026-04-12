def describe_pet(pet_name, animal_type='cat'):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")

describe_pet('pus')
describe_pet(animal_type='dog', pet_name='cane corso')

