word = "pizza"
print(
    """
    Tworzenie wycinkow
    0   1   2   3   4   5
      p   i   z   z   a
    """
)

print("Wprowadz poczatkowy i koncowy indeks lancucha 'pizza'")
print("Aby zakonczyc tworzenie wycinkow, w odpowiedzi na monit nacisnij enter\n")
start = None
while start != "":
    start=(input("\nPoczatek: "))
    if start:
        start = int(start)
        finish = int(input("Koniec: "))
        print("word[", start, ":", finish, "] to", end = " ")
        print(word[start:finish])
input("\nAby zakonczyc nacisnij enter.")