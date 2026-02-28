
# True and False
language = 'python'
if 'python' in language:
    print(True)

language = 'javascript'
if 'python' in language:
    print(True)
else:
    print(False)

# Access
hash_key = '000111000111'
if hash_key == '001111000111':
    print("Access granted!")
    print(True)
else:
    print("Access denied!")
    print(False)

print(f"\n --- \n")

# The bouncer
user = 13

if user in range(0, 18):
    print("Minors are not allowed entry!")
elif user in range(18, 65):
    print("Adults have access with an entry fee of $50")
else:
    print("Seniors have free access!")

print(f"\n --- \n")

# Grade Calculator

user_score = 55

if user_score in range(90, 101):
    grade = 'A'
if user_score in range(70, 90):
    grade = 'B'
if user_score in range(50, 70):
    grade = 'C'
if user_score in range(30, 50):
    grade = 'D'
if user_score in range(15, 30):
    grade = 'E'
if user_score in range(0, 15):
    grade = 'F'

print(f"You scored {user_score}, which means you passed with grade {grade}!")    

print(f"\n --- \n")

# Triangle Classifier

a = 15
b = 15
c = 15    

## Determining Triangle Validity

valid = []
invalid = []

if a + b > c:
    valid.append(1)
else:
    invalid.append(1)

if a + c > b:
    valid.append(1)
else:
    invalid.append(1)   

if b + c > a:
    valid.append(1)
else:
    invalid.append(1)

if sum(valid) == 3:
    print(f"\nThis is a valid Triangle because the result of valid conditions was: {sum(valid)}")
if sum(invalid) == 1:
    print(f"This is an invalid Triangle because the result of invalid conditions was: {sum(invalid)}, while valid conditions was {sum(valid)}")    

## Classifying the Triangle

if a == b == c:
    print("This Triangle is classified as Equilateral because all sides are the same length.")
elif (a == b) or (a == c) or (b == c):
    print("This Triangle is classified as Isosceles because two sides are the same lengths.")

if a != b != c and a != c:
    print("This Triangle is classified as Scalene because none of the sides have the same lengths.")         

print(f"\n --- \n")

# Shipping Cost Estimator  

package_weight = 45
destination = 'domestic'
shipping_type = 'standard'

price = []

if package_weight in range(0, 15):
    price.append(15)
elif package_weight in range(15, 30):
    price.append(20)
elif package_weight in range(30, 50):
    price.append(25)

if destination == 'domestic':
    price.append(5)
else:
    price.append(50)

if shipping_type == 'express':
    price.append(25)
else:
    price.append(5)

print(f"\nYour package weight is {package_weight}. You have chosen an {destination.title()} order with {shipping_type.title()} shipping.")
print(f"The shipping costs will be a total of: {sum(price)}.")

print(f"\n --- \n")

# Equality and Inequality

nurse = 'Noemi'

if nurse == 'nemo':
    print(True)
else:
    print(False, nurse)

if nurse.lower() == 'noemi':
    print(True)

print(f"\n --- \n")

num_nurse = 43

if num_nurse == 40:
    print(f"{True} {num_nurse}")
elif num_nurse >= 40:
    print(f"{True} {num_nurse}")
elif num_nurse <= 56:
    print(f"{True} {num_nurse}")
elif num_nurse == 55:
    print(f"{True} {num_nurse}")

if num_nurse >= 40 or num_nurse <= 40:
    print(f"Yes the number of nurses are in fact {num_nurse}")

if num_nurse == 43 and num_nurse <= 70:
    print(True)

print(f"\n --- \n")

awkward_list = ['I', 'Really', 'Think', 'This', 'Exercise', 'Is', 'Boring']

if 'Boring' in awkward_list:
    print('Boring')
else:
    print('Did not work properly')

if 'challenging' not in 'awkward_list':
    print("Aha - yes that explains why you think it's boring!")
else:
    print("Good that you thought this was challenging. I did not.")    