sandwich_orders = ['reuben', 'cubano', 'pastrami', 'banh mi', 'croque monsieur', 'philly cheesesteak',
                    'muffuletta', 'lobster roll', 'cemita', 'katsu sando', 'chopped cheese',
                    'francesinha', 'medianoche', 'reuben', 'pastrami', 'cubano', 'banh mi', 'croque monsieur', 
                    'philly cheesesteak', 'muffuletta', 'lobster roll', 'cemita', 'katsu sando', 'chopped cheese',
                    'francesinha', 'medianoche', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print("We are sorry to announce but we have run out of Pastrami!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Sending your order: {current_sandwich.title()}")
    finished_sandwiches.append(current_sandwich)

print("\n--- Orders Ready ---")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()}")   
