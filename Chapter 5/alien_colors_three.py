# Version one
alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

# Version two
alien_color = 'red'

if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
else:
    points = 15

print(f"You just earned {points} points!")

# Version three

from random import shuffle

alien_color = ['red', 'yellow', 'green']

shuffle(alien_color)

for points, color in enumerate(alien_color, 1):
    if color == 'yellow':
        score = 10
    elif color == 'red':
        score = 15
    elif color == 'green':
        score = 5      
    print(f"Since you are {color.title()}, then you just earned {score} points!")

# First try:
# Wow. I need to comment on this one. I really tried, but the knowledge to finish
# this couldn't seem to reach. Anyways, the problems here is quite severe but you
# can clearly see where my head was going. Unfortunatly the logic here is bad. 
# 
# Second try:
# Well. Clearly I found out how to use import, enumerate, and shuffle. I am 
# genuinely impressed of myself to be able to create & fix this logic.  

       