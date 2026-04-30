def order_sandwich(*products):
    '''Prints a order summary of a sandwich'''
    print("\nOrder Summary:")
    for product in products:
        print(f"- {product}")

order_sandwich('ham', 'butter', 'lettuce')
order_sandwich('chicken', 'dressing', 'lettuce', 'cheese')
order_sandwich('turkey', 'cheese')        