import os


def get_symbols():
    while True:
        player1 = input(
            "Player 1, please pick [X] or [O] as your symbol ").upper()
        if player1 == "X" or player1 == "O":
            break
        else:
            print("Not a valid symbol.")
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
    return player1, player2, player1


def win_condition(dc):
    win = [
        (dc["7"], dc["8"], dc["9"]),
        (dc["4"], dc["5"], dc["6"]),
        (dc["1"], dc["2"], dc["3"]),
        (dc["7"], dc["4"], dc["1"]),
        (dc["8"], dc["5"], dc["2"]),
        (dc["9"], dc["6"], dc["3"]),
        (dc["7"], dc["5"], dc["3"]),
        (dc["1"], dc["5"], dc["9"])
    ]
    for i in win:
        if i[0] + i[1] + i[2] == "XXX" or i[0] + i[1] + i[2] == "OOO":
            return True
    return False


def is_tie(dc):
    return all((i != " " for i in dc.values()))


def enter_symbol(p, dc):

    def validation(keypress):
        if keypress in '123456789':
            if dc[keypress] == " ":
                return True
            else:
                print("Field is not empty. Please pick another field.")
                return False

        else:
            print("Invalid input. Please enter a number.")
            return False

    while True:
        keypress = input(f"Mark a field with {p}. ")
        if validation(keypress):
            dc[keypress] = p
            break
    return dc


def print_field(dc):
    os.system('cls')
    em = "   |   |   \n"
    spacer = "___|___|___\n"
    row1 = f' {dc["7"]} | {dc["8"]} | {dc["9"]} \n'
    row2 = f' {dc["4"]} | {dc["5"]} | {dc["6"]} \n'
    row3 = f' {dc["1"]} | {dc["2"]} | {dc["3"]} \n'
    field = em + row1 + spacer + em + \
        row2 + spacer + em + row3 + em + '\n'
    print(field, end='')


def play(dc):
    player1, player2, active_player = get_symbols()
    while True:
        print_field(dc)
        dc = enter_symbol(active_player, dc)
        if win_condition(dc):
            if active_player == player1:
                print_field(dc)
                print("Player 1 wins!")
            else:
                print_field(dc)
                print("Player 2 wins!")
            break
        if is_tie(dc):
            print_field(dc)
            print("It's a tie!")
            break
        if active_player == player1:
            print("Your turn, Player 2")
            active_player = player2
        else:
            print("Your turn, Player 1")
            active_player = player1


def play_again():
    while True:
        answer = input("Do you want to play again? ")
        if answer[0].lower() == "y":
            return True
        elif answer[0].lower() == "n":
            return False
        else:
            print("Yes or No?")


def reset_game(dc):
    return


dc = {"1": " ", "2": " ", "3": " ", "4": " ",
      "5": " ", "6": " ", "7": " ", "8": " ", "9": " "}

while True:
    play(dc)
    if not play_again():
        break
    else:
        # Reset the game
        dc = dc.fromkeys([str(i) for i in range(1, 10)], " ")
