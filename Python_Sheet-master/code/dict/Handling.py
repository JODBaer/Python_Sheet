cb300 = {
    'brand':    'honda',
    'color':    'red',
    'power':    (31, 'hp')
    }
keys = ('year', 'weight')
values = 0
print(cb300.items())
print(cb300.keys())
print(cb300.values())
print(cb300.get('color', 'raw'))
print(cb300.get('mileage', 0))
print(cb300.setdefault('color', 'black'))
cb300.update(dict.fromkeys(keys, values))
print(cb300)