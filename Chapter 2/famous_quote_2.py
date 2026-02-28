### Creates the Author as a variable and stores it. Creates two new variables to store the quote, and uses an f-string
### to use the Author variable inside a string. Combines both quote variables, and prints the message. 

author = "Marcus Aurelius"

quote1 = f'{author} once said: "The impediment to action advances action.'
quote2 = 'What stands in the way becomes the way."'

message = f"{quote1} {quote2}"

print(message)