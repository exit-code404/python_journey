def build_person(first_name, last_name, age='None'):
    '''Return a dictionary of information about a person.'''
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('james', 'bond', age=41)
print(musician)

second_musician = build_person('anastasia', 'bond')
print(second_musician)