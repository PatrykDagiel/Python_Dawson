inventory =  (
    "miecz",
    "zbroja",
    "tarcza",
    "napoj uzdrawiajacy")

print("\nElementy Twojego Wyposazenia:")
for item in inventory:
    print(item)

print("Twoj dobytek zawiera", len(inventory), "elementow(-y).")

if "napoj uzdrawiajacy" in inventory:
    print("Posiadasz napoj uzdrawiajacy")

index = int(input('\nWprowadz indeks elementu inwentarza:' ))
print("Pod indeksem", index, 'znajduje sie', inventory[index])

#wyswietl wycinek
start = int(input("\nWprowadz indeks wyznaczajacy poczatek wycinka: "))
finish = int(input('\nWprowadz indeks wyznaczajacy koniec wycinka: '))
print("inventory[", start, ":", finish, "] to", end=" ")
print(inventory[start:finish])

chest = ("zloto", "klejnoty")
print("znajdujesz skrzynie, ktora zawiera:")
print(chest)
print("Dodajesz zawartosc skrzyni do swojego inwentarza")
inventory += chest
print("Twoj aktualny inwentarz to:")
print(inventory)


input("\n\nAby zakonczyc program, nacisnij klawisz enter")