bundesraete=['Ueli Maurer', 'Ehrenglatze Berset']
with open('mytextfile.txt', 'w', encoding='utf-8') as f:
    f.writelines(bundesraete)