#Pusta krotka
inventory = ()

if not inventory:
    print("Nie posiadasz niczego")

input("\nAby kontynuowac misje, nacisnij klawisz Enter")
inventory =  ("miecz","zbroja","tarcza","napoj uzdrawiajacy")

print("\nWykaz zawartosci krotki")
print(inventory)

print("\nElementy Twojego Wyposazenia:")
for item in inventory:
    print(item)

input("\n\nAby zakonczyc program, nacisnij klawisz enter")