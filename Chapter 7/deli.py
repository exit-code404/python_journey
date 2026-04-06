sandwich_orders = ['reuben', 'cubano', 'banh mi', 'croque monsieur', 'philly cheesesteak',
                    'muffuletta', 'lobster roll', 'cemita', 'katsu sando', 'chopped cheese',
                    'francesinha', 'medianoche']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Sending your order: {current_sandwich.title()}")
    finished_sandwiches.append(current_sandwich)

print("\n--- Orders Ready ---")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()}")   
