def display_instruction():
    """Wyswietl instrukcje gry."""
    print("""
    Kolko i krzyzyk.
    Swoje posuniecie wskazujesz poprzez podanie liczby z zakresu 0 - 8.
    Odpowiadac to bedzie pozycji zgodnie ze schematem:
        0 | 1 | 2
        4 | 5 | 6
        6 | 7 | 8
    """)

def ask_yes_no(question):
    """Zadaj pytanie, na ktore mozna odpowiedziec tak lub nie"""
    answer = None
    while answer not in ('t', 'n'):
        answer = input(question).lower()
    return answer

def ask_number(question, low, high):
    """Podaj liczbe z odpowiedniego zakresu"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def pieces():
    """Ustal, do kogo nalezy pierwszy ruch"""
    go_first = ask_yes_no("Czy chcesz miec prawo pierwszego ruchu (t/n)")
    if go_first == 't':
        print('\nPierwszy ruch nalezy do Ciebie')
        human = X
        computer = O
    else:
        print("\nPierwszy ruch nalezy do komputera")
        computer = X
        human = O
    return computer, human

def new_board():
    """Utworz plansze do gry"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """Wyswietl plansze do gry na ekranie"""
    print('\n\t', board[0], board[1], board[2])
    print('\t', "------")
    print('\t', board[3], board[4], board[5])
    print('\t', "------")
    print('\t', board[6], board[7], board[8], '\n')


def legal_moves(board):
    """Tworzy liste prawidlowych ruchow"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    """Ustala zwyciezce gry"""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6),
                   )
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None

def human_move(board, human):
    """Odczytaj ruch czlowieka"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Jaki bedzie Twoj ruch? (0-8):", 0, NUM_SQUARES)
        if move not in legal:
            print('\nTo pole jest juz zajete, wybierz inne.\n')
    print("Znakomicie")
    return move

def computer_move(board, computer, human):
    """Spowoduj wykonanie ruchu przez komputer"""
    board = board[:]    #Kopia robocza aktualnej tablicy
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Wybieram pole numer", end=" ")
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY #Wycofanie
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

def next_turn(turn):
    """Zmienia wykonawce ruchu"""
    if turn == X:
        return O
    else:
        return X

def congrat_winner(the_winner, computer, human):
    """Gratulacje dla zwyciezcy"""
    if the_winner != TIE:
        print(the_winner, "jest zwyciezca!")
    else:
        print("Remis")
    if the_winner == computer:
        print("Jak przewidywalem, Czlowieku, jeszcze raz zostalem triumfatorem! \n"
              "Dowod na to, ze jestem lepszy")
    elif the_winner == human:
        print("Udalo ci sie wygrac. \n")
    elif the_winner == TIE:
        print("Miales mnostwo szczescia, Czlowieku. Udalo Ci sie zremisowac")

#Stale globalne
X = 'X'
O = 'O'
EMPTY = ' '
TIE = 'TIE'
NUM_SQUARES = 9


def main():
    display_instruction()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

main()
input("Aby zakonczyc gre, nacisnij enter")
