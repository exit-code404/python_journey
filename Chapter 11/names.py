from name_function import get_formatted_name

print("Enter 'q' to exit the program.")
while True:
    first = input("\nWhat is your first name? ")
    if first == 'q':
        break
    last = input("\nWhat is your last name? ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted full name: {formatted_name}")