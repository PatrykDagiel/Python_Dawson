message = input("Wprowadz komunikat: ")
new_message = ""
VOWELS = "aeuioy"
print()
for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print("Zostal utworzony lancuch ", new_message)

print("\nTwoj komunikat bez samoglosek to:", new_message)
input('\n\nAby zakonczyc wcisnij enter')