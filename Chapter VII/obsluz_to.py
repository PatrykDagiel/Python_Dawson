#try/except
try:
    num = float(input("Wprowadz liczbe zmiennoprzecinkowa: "))
except ValueError:
    print("Wystapil jakis blad")

print()
for value in (None, "Hej"):
    try:
        print("Proba konwersji:", value, "--->", end="")
        print(float(value))
    except (TypeError, ValueError):
        print('Wystapil jakis blad')

try:
    num = float(input('Wprowadz liczbe: '))
except ValueError as e:
    print("To nie byla liczba, tylko: ")
    print(e)
else:
    print('Wprowadziles poprawnie', num)

input('Enter, aby zakonczyc')