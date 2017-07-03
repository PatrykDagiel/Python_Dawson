import pickle, shelve
print('Marynowanie list')
variety = ['lagodny', 'pikantny', 'kwaszony']
shape = ['caly', 'krojony wzdluz', 'w plasterkach']
brand = ['Dawtona', 'Klimex', 'Vortumns']
f = open('pikiel.dat', "wb")
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()
print('\nOdmarowywanie list')
f = open('pikiel.dat', "rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)

print(variety)
print(shape)
print(brand)
f.close()

print('\nOdkladanie list na polke')
s = shelve.open('pikle2.dat')
s["odmiana"] = ['lagodny', 'pikantny', 'kwaszony']
s["ksztalt"] = ['caly', 'krojony wzdluz', 'w plasterkach']
s["marka"] = ['Dawtona', 'Klimex', 'Vortumns']
s.sync()

print('Pobieranie wartosci z polki')
print('marka -', s['marka'])
print('ksztalt -', s['ksztalt'])
print('odmiana -', s['odmiana'])
s.close()



