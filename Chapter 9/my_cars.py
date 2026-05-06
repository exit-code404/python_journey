import car as c

my_eqs = c.ElectricCar('Merchedes', 'EQS', 2026)
print(my_eqs.get_descriptive_name())
my_eqs.battery.describe_battery()
my_eqs.battery.get_range()

my_eqs.battery.upgrade_battery()

my_eqs.battery.describe_battery()
my_eqs.battery.get_range()

my_porsche = c.Car('porsche', 'GT3', 2020)
print(my_porsche.get_descriptive_name())