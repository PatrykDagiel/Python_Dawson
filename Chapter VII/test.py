import sys

def open_file(file_name, mode):
    """Otworz plik"""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Nie mozna otworzyc pliku", file_name, "Program zostanie zakonczony: \n", e)
        input("Aby zakonczyc program nacisnij enter")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Zwroc kolejny wiersz pliku kwiz po sformatowaniu go"""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Zwroc kolejny blok danych z pliku kwiz"""
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    return category, question, answers, correct, explanation