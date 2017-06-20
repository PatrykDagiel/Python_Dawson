#Demonstruje metody listy w pythonie
scores = []
choice = None

while choice != "0":
    print(
        """
        Najlepsze wyniki.
        1 - pokaz wyniki
        2 - dodaj wynik
        3 - usun wynik
        4 - posortuj wyniki
        """
    )
    choice = input("Wybierasz: ")
    print()
    if choice == "0":
        print("Do widzenia")
    elif choice == '1':
        print("Najlepsze wyniki")
        for score in scores:
            print(score)
    elif choice == '2':
        score = int(input("Jaki wynik uzyskales?: "))
        scores.append(score)
    elif choice == "3":
        score = int(input("Ktory wynik usunac?: "))
        if score in scores:
            scores.remove(score)
        else:
            print(score, "nie ma na liscie wynikow.")
    elif choice == '4':
        scores.sort(reverse=false)
    else:
        print("Nieznana opcja")

