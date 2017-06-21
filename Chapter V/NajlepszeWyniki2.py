#Sekwencje zagniezdzone
scores = []
choice = None
while choice != '0':
    print(
        """
        Najlepsze wyniki.
        1 - pokaz wyniki
        2 - dodaj wynik
        """
    )
    choice = input("Wybierasz: ")
    print()
    if choice == '0':
        print("Exit")
    elif choice == '1':
        print('Najlepsze wyniki:\n')
        print("Gracz\tWynik")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)
    elif choice == '2':
        name = input("Podaj nazwe gracza:")
        score = int(input("Jaki wynik uzyskal gracz:"))
        entry = (score, name)
        scores.append(entry)
        scores.sort(revert=True)
        scores = scores[:5]
    else:
        print("Nieznana opcja")

input("Aby zakonczyc nacisnij enter")