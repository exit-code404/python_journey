def greet_users(names):
    '''Print a single greeting to each user in a list'''
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['noemi', 'camilo', 'ida']
greet_users(usernames)        