import random
word = "indeks"

high=len(word)
low=-len(word)
for i in range(10):
    position = random.randrange(low, high)
    print("word[", position, "]\t", word[position])

input("\nAby zakonczyc program nacisnij enter")