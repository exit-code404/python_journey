def build_car(manufacturer, model_name, **kwargs):
    '''Builds a dictionary with car information'''
    kwargs['manufacturer'] = manufacturer
    kwargs['model name'] = model_name
    return kwargs

car_specs = build_car('polestar', '4', electric='Yes', horsepower='600 hk', color='matte black')

print(car_specs)