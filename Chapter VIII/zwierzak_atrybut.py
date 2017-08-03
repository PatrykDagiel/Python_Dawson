class Critter(object):
    def __init__(self, name):
        print("Urodzil sie nnowy zwierzak")
        self.name = name

    def __str__(self):
        rep = "Obiekt klasy Critter \n"
        rep += "name: " + self.name
        return rep

    def talk(self):
        print('Czesc, jestem', self.name, '\n')

crit1 = Critter('Reksio')
crit1.talk()

crit2 = Critter("Pucek")
crit2.talk()

print('Bezpsorednie wyswietlenie parametru name obiektu 1: ', crit1.name)
input('Aby zakonczyc nacisnij enter')