def birthday1(name, age):
    print("Szczesliwych urodzin", name, '!', ' Masz juz', age, "lat\n")

def birthday2(name = "Janusz", age = 5):
    print("Szczesliwych urodzin", name, '!', ' Masz juz', age, "lat\n")

birthday1("Janusz", 5)
birthday1(5, 'Janusz')
birthday1(name="Janusz", age=5)
birthday1(age = 5, name = "Janusz")

birthday2()
birthday2(name = "Katarzyna")
birthday2(age = 12)
birthday2(name = "Katarzyna", age = 12)
birthday2("Katarzyna", 12)
