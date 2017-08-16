class Critter(object):
    """Wirtualny pupil"""
    def __init__(self, name):
        print('Urodzil sie nowy zwierzak')
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print('Pusty lancuch - nie mozna przypisac')
        else:
            self.__name = new_name
            print('Zmiana sie powiodla')