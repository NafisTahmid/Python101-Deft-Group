cars = {
    'models':2027,
    'made':'USA',
    'color':'red'
}

# cars['made'] = 'Korea'
# cars.update({'made':'Japan'})
cars['brand'] = 'Toyota'
cars.update({'brand':'Tesla'})
print('Old cars dictionary:', cars)
cars.pop('models')
cars.popitem()
print(cars)
