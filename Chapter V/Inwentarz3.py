inventory = ['miecz', 'zbroja', 'tarcza', 'napoj uzdrawiajacy']

print("Elementy Twojego inwentarza: ")
for item in inventory:
    print(item)

print("Twoj dobytek zawiera", len(inventory), "elementow")

if 'napoj uzdrawiajacy' in inventory:
    print("\nPosiadasz napoj uzdrawiajacy")

#Konkatenacja list
chest = ["zloto", "klejnoty"]
print("Znajdujesz skrzynie, ktora zawiera:")
print(chest)
inventory += chest
inventory[0] = "kusza"
print("Zamieniles tez miecz na kusze. Twoj aktualny inwentarz to:")
print(inventory)

print("Zuzywasz zloto i klejnoty na zakup kuli do wrozenia")
inventory[4:6] = ["kula do wrozenia"]

del inventory[2]
print("Tracisz tez tarcze")

print("Twoj aktualny inwentarz to:")
print(inventory)


input("\nAby zakonczyc nacisnij enter")