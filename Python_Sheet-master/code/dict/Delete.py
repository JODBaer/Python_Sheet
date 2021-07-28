cb300 = {
    'brand':    'honda',
    'color':    'red',
    'power':    (31, 'hp')
    }
print(cb300.pop('color', 'raw'))
print(cb300.pop('color', 'raw'))
print(cb300.popitem())  #removes last added item
cb300.clear()
print(cb300)