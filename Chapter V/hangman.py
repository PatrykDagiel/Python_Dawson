import random

HANGMAN = (
    """
    __________
    |        |
    |
    |
    |
    |
    |
    __________
    """,
    """
    __________
    |        |
    |        o
    |
    |
    |
    |
    __________
    """,
    """
    __________
    |        |
    |        o
    |       ---
    |
    |
    |
    __________
    """,
    """
    __________
    |        |
    |        o
    |       ---
    |        +
    |
    |
    __________
    """,
    """
       __________
       |        |
       |        o
       |       ---
       |        +
       |       /
       |
       __________
    """,
    """
       __________
       |        |
       |        o
       |       ---
       |        +
       |       / /
       |
       __________
    """
)

MAX_WRONG = len(HANGMAN) - 1

WORDS = ("MALZ", "MATKA", "KALAFIOR", "POMIDOR")

word = random.choice(WORDS)
so_far = "-" * len(word)
wrong = 0   #liczba nietrafionych liter
used = []   # tablica uzytych liter

print("Gra szubienica \n")
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\n Wykorzystales nastepujace litery:", used)
    print("\n Na razue slowo wyglada tak:", print)
    guess = input("\n\nWprowadz litere: ")
    guess = guess.upper()
    while guess in used:
        print("Juz wykorzystales litere", guess)
        guess = input("Wprowadz litere: ")
        guess = guess.upper()
    used.append(guess)

    if guess in word:
        print("Litera", guess, "znajduje sie w slowie")
        new = ""    #kopia so_far
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("Niestety", guess, "nie ma w zagadkowym slowie")
        wrong += 1
    if wrong == MAX_WRONG:
        print(HANGMAN[wrong])
        print("\nZostales powieszony")
    else:
        print("\nOdgadles")
print("Zagadkowe slowo to", word)
input("Aby zakonczyc nacisnij enter")
