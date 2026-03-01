fav_fruits = ['mango', 'dragonfruit', 'pineapple', 'banana', 'strawberry', 'peach']

points = []

if 'strawberry' in fav_fruits:
    points.append(1)

if 'apple' in fav_fruits:
    points.append(1)

if 'banana' in fav_fruits:
    points.append(1)

if 'blueberries' in fav_fruits:
    points.append(1)

if 'mango' in fav_fruits:
    points.append(1)

fruits = sum(points)
sum_fruits = len(fav_fruits)

print(f"You must really like fruits! Our tests shows that we guessed {fruits}/{sum_fruits} correct times. We had a total of 5 tests.")                    