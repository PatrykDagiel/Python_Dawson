print("Utworzenie pliku tekstowego za pomoca metody write().")
text_file = open("zapisz_to.txt", "w")
text_file.write("Wiersz 1\n")
text_file.write("To jest wiersz 2\n")
text_file.write("Ten tekst tworzy wiersz 3\n")
text_file.close()

print("\nDodanie informacji do pliku za pomoca writelines()")
text_file = open("zapisz_to.txt", "a")
lines = ["Wiersz 1\n", "To jest wiersz 2\n", "A to trzeci\n"]
text_file.writelines(lines)
text_file.close()

print("\nOdczytanie zawartosci nowo utworzonego pliku.")
text_file = open("zapisz_to.txt", "r")
print(text_file.read())
text_file.close()
