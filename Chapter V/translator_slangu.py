geek = {
    "404" : "googlowanie; wyszukiwanie w internecie informacji dotyczacych jakiejs osoby.",
    "googling" : "googlowanie, poszukiwanie odpowiedzi na internecie",
    "keyboard plaque" : "(skojarzone z kamieniem nazebnym)zanieczyszczenia nagromadzone na klawiaturze komputera",
    "Link Rot" : "Obumieranie linkow, proces w ktorym linki do stron www staja sie nieaktualne",
    "Percussive maintenance" : "(konserwacja perkusyjna)naprawa urzadzenia elektronicznego przez stukniecie",
    "uninstalled" : "Zwolniony z pracy, odinstalowany, popularne w okresie banki internetowej"
}
#Komentarzyk
if "Dancing Baloney" in geek:
    print("Wiem, co to jest Dancing Baloney.")
else:
    print("Nie mam pojecia co to jest DB")
print(geek.get("Dancing Baloney"))
choice = None
while choice != "0":
    print(
        """"
        Translator slangu komputerowego
        0 - zakoncz
        1 - znajdz nowy termin
        2 - dodaj nowy termin
        3 - zmien definicje terminu
        4 - usun termin
        """
    )
    choice = input('Wybierasz:')
    print()
    if choice == "0":
        print("Zegnaj")

    elif choice == '1':
        term = input("Jaki termin mam przetlumaczyc?")
        if term in geek:
            definition = geek[term]
            print("\n", term, "oznacza", definition)
        else:
            print("Niestety, nie znam terminu")
    elif choice == '2':
        term = input("Jaki termin mam dodac?")
        if term not in geek:
            definition = input("\nPodaj definicje tego terminu")
            geek[term] = definition
            print(term, "zostal dodany")
        else:
            print("Termin juz istnieje, zmien jego definicje")
    elif choice == '4':
        term = input("Jaki termin mam usunac: ")
        if term in geek:
            del geek[term]
            print("\nOk, usunieto", term)
        else:
            print("\nNie moge tego zrobic, terminu", term, "nie ma w slowniku")
    else:
        print('Nieznna opcja')
input("Aby zakonczyc nacisnij enter")