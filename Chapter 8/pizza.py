def make_pizza(size, *toppings):
    '''Print the list of toppings that have been requested'''
    print(f"\nMaking a {size}-centimeter pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(30, 'pepperoni')
make_pizza(40, 'cheese', 'ham', 'champingnon')

# Note: I will notice the parameter name *args, which collects arbitrary positional 
# arguments like this.
