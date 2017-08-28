#Opiekun zwierzaka
#Wirtualny pupil, ktorym nalezy sie opiekowac

class Critter(object):
    """Wirtualny pupil"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "szczesliwy"
        elif 5 <= unhappiness <= 10:
            m = "zadowolony"
        elif 11 <= unhappiness <= 15:
            m = "zly"
        else:
            m = "wsciekly"
        return m
    def talk(self):
        print("Nazywam sie", self.name, "i jestem", self.mood, "teraz\n")
        self.__pass_time()
    def eat(self, food = 4):
        print("Mniam, mniam. Dziekuje")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
    def play(self, fun = 4):
        print("Hura!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input("Jak chcesz nazwac swojego zwierzaka?: ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print \
            ("""
            Opiekun zwierzaka
            0 - zakoncz
            1 - sluchaj swojego zwierzaka
            2 - nakarm swojego zwierzaka
            3 - pobaw sie ze swoim zwierzakiem
            """)
        choice = input("Wybierasz: ")
        print()

        if choice == "0":
            print("Do widzenia")
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            crit.eat()
        elif choice == "3":
            crit.play()
        else:
            print("\nNieznany wybor")

main()
input("\nAby zakonczyc program, nacisnij klawisz enter")