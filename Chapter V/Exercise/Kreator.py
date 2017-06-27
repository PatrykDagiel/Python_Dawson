PUNKTY_DO_DYSTRYBUCJI = 30

Atrybuty = {'Sila' : 0, 'Zdrowie': 0, 'Madrosc' : 0, 'Zrecznosc' : 0}
choice = None
wartosc = None

while(PUNKTY_DO_DYSTRYBUCJI != 0):
    print("Masz", PUNKTY_DO_DYSTRYBUCJI ,"punktow, przydziel je.")
    print(
    """
    1 - Dodaj sile
    2 - Dodaj zdrowie
    3 - Dodaj madrosc
    4 - Dodaj zrecznosc
    0 - Wyjdz
    """
    )
    print("Twoje atrybuty to: ", Atrybuty)
    choice = input("Wybierasz: ")
    if choice == '1':
        wartosc = int(input("Ile sily chcesz dodac?: "))
        if PUNKTY_DO_DYSTRYBUCJI - wartosc >= 0:
            Atrybuty['Sila'] += wartosc
            PUNKTY_DO_DYSTRYBUCJI -= wartosc
    elif choice == '2':
        wartosc = int(input("Ile zdrowia chcesz dodac?: "))
        if PUNKTY_DO_DYSTRYBUCJI - wartosc >= 0:
            Atrybuty['Zdrowie'] += wartosc
            PUNKTY_DO_DYSTRYBUCJI -= wartosc
    elif choice == '3':
        wartosc = int(input("Ile madrosci chcesz dodac?: "))
        if PUNKTY_DO_DYSTRYBUCJI - wartosc >= 0:
            Atrybuty['Madrosc'] += wartosc
            PUNKTY_DO_DYSTRYBUCJI -= wartosc
    elif choice == '4':
        wartosc = int(input("Ile zrecznosci chcesz dodac?: "))
        if PUNKTY_DO_DYSTRYBUCJI - wartosc >= 0:
            Atrybuty['Zrecznosc'] += wartosc
            PUNKTY_DO_DYSTRYBUCJI -= wartosc
    elif choice == '0':
        exit(0)
    else:
        print('Brak opcji.')
input("Aby zakonczyc nacisnij enter")



