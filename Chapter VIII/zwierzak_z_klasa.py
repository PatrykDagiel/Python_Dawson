#Demonstruje metody statyczne i atrybuty klasy
class Critter(object):
    """"Wirtualny pupil"""
    total = 0

    @staticmethod
    def status():
        print("Ogolna liczba zwierzakow wynosi", Critter.total)

    def __init__(self, name):
        print('Urodzil sie zwierzak')
        self.name = name
        Critter.total += 1

print('Uzyskanie dostepu do atrybutu klasy Critter.total', end= " ")
print("Critter.total")

print("\nTworzenie zwierzakow")
crit1 = Critter('zwierzak 1')
crit3 = Critter('zwierzak 2')
crit2 = Critter('zwierzak 3')

Critter.status()
print("\nUzyskanie dostepu do atrybutu klasy poprzez obiekt,", end= " ")
print(crit1.total)

input('\nAby zakonczyc nacisnij enter')