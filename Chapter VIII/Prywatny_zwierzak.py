#Demonstruje zmienne i metody prywatne
class Critter(object):
    """Wirtualny pupil"""
    def __init__(self, name, mood):
        print('Urodzil sie niey zwierzak!')
        self.name = name
        self.__mood = mood  #Atrybut prywatny
    def talk(self):
        print('\nJestem', self.name)
        print('W tej chwili czuje sie', self.__mood, '\n')
    def __private_method(self):
        print('To jest metoda prywatna.')
    def public_method(self):
        print('To jest metoda publiczna')
        self.__private_method()

crit = Critter(name='Reksio', mood='szczesliwy')
crit.talk()
crit.public_method()