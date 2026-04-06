pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'dog', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
    pets.remove('dog')

print(pets)    