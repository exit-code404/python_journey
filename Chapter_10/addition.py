active = True

while active:

    print("Press 'q' to exit the program.")

    addition = input("Give me a number: ")
    if addition == 'q':
        break
    addition2 = input("Give me another number: ")
    if addition2 == 'q':
        break

    try:
        result = int(addition) + int(addition2)
    except ValueError:
        print("Only numbers accepted.")
    else:
        print(result)