import random

#sekwencja slow do wyboru
WORDS = ("python", "anagram", "latwy", "skomplikowany", "odpowiedz", "ksylofon")
word = random.choice(WORDS)
correct = word

anagram = ""
while word:
    position = random.randrange(len(word))
    anagram += word[position]
    word = word[:position] + word[(position + 1):]

print("\nZgadnij, jakie to slowo: ", anagram)
guess = ("\nTwoja odpowiedz: ")
while guess != correct and guess != "":
    print("Niestety, to nie to slowo")
    guess = input("Twoja odpowiedz ")

input("\nDobrze, aby zakonczyc, nacisnij Enter.")