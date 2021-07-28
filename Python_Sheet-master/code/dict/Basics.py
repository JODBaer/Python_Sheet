cb300 = {
    'brand':    'honda',
    'color':    'red',
    'power':    (31, 'hp')
    }
update = {'category': 'naked'}
cb300['mileage[km]'] = 3148
cb300['mileage[km]'] = 4399
cb300.update(update)
cb500 = cb300.copy()
cb500['power'] = (48, 'hp')
cb500['color'] = 'grey'
print(cb300)
print(cb500)