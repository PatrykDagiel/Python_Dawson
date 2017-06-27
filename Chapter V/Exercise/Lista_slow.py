import random
lista = ["tata", "mama", "wujek", "babcia"]
wypisane = []
while lista and (len(wypisane) != 4):
    slowo = random.choice(lista)
    print("Jeden z elementow listy:", slowo)
    wypisane.append(slowo)
    lista.remove(slowo)
    print("pozostala lista:", lista)
    print("Wypisane:", wypisane)