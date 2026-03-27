is_ten = input("Enter a number and I will tell you if it's a multiple of ten or not: ")
is_ten = int(is_ten)

if is_ten % 10 == 0:
    print(f"The number {is_ten} is a multiple of ten.")
else:
    print(f"The number {is_ten} is not a multiple of ten.")