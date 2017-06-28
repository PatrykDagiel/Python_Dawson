def read_global():
    print("Wartosc zmiennej value odczytana wewnatrz zakresu lokalnego",
          "\nfunkcji read_global() wynosi:", value)
def shadow_global():
   value = -10
   print("Wartosc zmiennej value odczytana wewnatrz zakresu lokalnego",
         "\nfunkcji change_global() wynosi: ", value)

def change_global():
    global value
    value = -10
    print("Wartosc zmiennej value odczytana wewnatrz zakresu lokalnego",
          "\nfunkcji change_global(), wynosi: ", value)

value = 10
print("Zakres globalny, ustawienie:", value)
read_global()
print("Po powrocie do zakresu globalnego wartosc nadal wynosi:", value, "\n")

shadow_global()
print("Po powrocie do zakresu globalnego wartosc nadal wynosi:", value, "\n")

change_global()
print("Po powrocie do zakresu globalnego i zmianie wartosc nadal wynosi:", value, "\n")

input("\n\nAby zakonczyc prace programu, nacisnij enter")

