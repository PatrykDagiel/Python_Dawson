class Player(object):
    """Gracz w grze strzelance"""
    def blast(self, enemy):
        print("Gracz razi wroga")
        enemy.die()

class Alien(object):
    """Obcy w grze strzelance"""
    def die(self):
        print("Finish")

hero = Player()
invader = Alien()
hero.blast(invader)

input('Aby zakonczyc program, nacisnij enter')