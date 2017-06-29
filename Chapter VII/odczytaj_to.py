print('Otwarcie i zamkniecie pliku')
text_file = open("../Resources/odczytaj_to.txt", "r")
text_file.close()

print('\nOdczytywanie znakow z pliku')
text_file = open("../Resources/odczytaj_to.txt", "r")
print(text_file.read(1))
print(text_file.read(7))
text_file.close()

print("\nOdczytanie calego pliku za jednym razem")
text_file = open("../Resources/odczytaj_to.txt", "r")
whole_thing = text_file.read()
print(whole_thing)
text_file.close()

print("\nOdczytywanie znakow z wiersza")
text_file = open("../Resources/odczytaj_to.txt", 'r')
print(text_file.readline(1))
print(text_file.readline(7))
text_file.close()

print("\nOdczytywanie po jednym wierszu na raz")
text_file = open("../Resources/odczytaj_to.txt", 'r')
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()

print("\nWczytanie calego pliku do listy")
text_files = open("../Resources/odczytaj_to.txt", 'r')
lines = text_files.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line)
text_file.close()

print('\nPobieranie zawartosci pliku wiersz po wierszu przy uzyciu petli.')
text_file = open("../Resources/odczytaj_to.txt", 'r')

input("Aby zakonczyc program, nacisnij enter")
