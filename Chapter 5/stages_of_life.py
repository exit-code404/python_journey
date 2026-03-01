age = 21

if age < 2:
    stage = "a Baby"
elif age < 4:
    stage = "a Toddler"
elif age < 13:
    stage = "a Kid"
elif age < 20:
    stage = "a Teenager"
elif age < 65:
    stage = "an Adult"
else:
    stage = "an Elder"

print(f"Since you are {age} years old. That means you are {stage}.")     

