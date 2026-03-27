rental_car = input("Please enter the car you would like to rent: ")
print(f"Let me see if I can find you a {rental_car}.")

if rental_car == 'bmw':
    print(f"It does seem like we do have {rental_car}")
elif rental_car == 'merchedes':
    m_version = input(f"We do have both the Brabus and regular version of this car. Which would you like? ")
    print(f"You have chosen: {rental_car} in the {m_version} version.")
