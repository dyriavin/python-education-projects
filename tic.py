X_POINT = 'X'
O_POINT = 'O'


def draw_result(cells):
    print("""
    ---------
    | {0} {1} {2} |
    | {3} {4} {5} |
    | {6} {7} {8} |
    ---------
    """.format(*cells))


def is_x_wins(cells):
    first_horizontal = cells[0:3]
    second_horizontal = cells[3:6]
    third_horizontal = cells[6:9]
    # make diagonal arrays
    first_diagonal = cells[0::3]
    second_diagonal = cells[2:-1:2]
    # make row arrays
    first_row = cells[0::3]
    second_row = cells[1::3]
    third_row = cells[2::3]

    horizontal = first_horizontal.count(X_POINT) == 3 or second_horizontal.count(
        X_POINT) == 3 or third_horizontal.count(X_POINT)
    diagonal = first_diagonal.count(X_POINT) == 3 or second_diagonal.count(X_POINT) == 3
    row = first_row.count(X_POINT) == 3 or second_row.count(X_POINT) == 3 or third_row.count(X_POINT) == 3
    if horizontal is True or diagonal is True or row is True:
        return True
    else:
        return False


def is_o_wins(cells):
    first_horizontal = cells[0:3]
    second_horizontal = cells[3:6]
    third_horizontal = cells[6:9]
    # make diagonal arrays
    first_diagonal = cells[0::3]
    second_diagonal = cells[2:-1:2]
    # make row arrays
    first_row = cells[0::3]
    second_row = cells[1::3]
    third_row = cells[2::3]

    horizontal = first_horizontal.count(O_POINT) == 3 or second_horizontal.count(
        O_POINT) == 3 or third_horizontal.count(O_POINT)
    diagonal = first_diagonal.count(O_POINT) == 3 or second_diagonal.count(O_POINT) == 3
    row = first_row.count(O_POINT) == 3 or second_row.count(O_POINT) == 3 or third_row.count(O_POINT) == 3
    if horizontal is True or diagonal is True or row is True:
        return True
    else:
        return False


def is_not_game_finished(cells):
    if is_x_wins(cells) is not True and is_o_wins(cells) is not True and cells.count('_') == cells.count(
            X_POINT) and cells.count('_') == cells.count(O_POINT):
        return True
    else:
        return False


def is_impossible_case(cells):
    if is_x_wins(cells) is True and is_o_wins(cells) is True:
        return True
    elif cells.count(X_POINT) == 3 and cells.count(O_POINT) < 3 or cells.count(O_POINT) == 3 and cells.count(
            X_POINT) < 3:
        return True
    elif cells.count(X_POINT) > 3 and cells.count(O_POINT) < 3 or cells.count(O_POINT) > 3 and cells.count(X_POINT) < 3:
        return True
    else:
        return False


def initialize(cells):
    if is_not_game_finished(cells) is True:
        draw_result(cells)
        print("Game not finished")
    elif is_impossible_case(cells) is True:
        draw_result(cells)
        print("Impossible")
    else:
        if is_x_wins(cells) is not False:
            draw_result(cells)
            print("X wins")
        elif is_o_wins(cells):
            draw_result(cells)
            print("O wins")
        elif cells.count('_') == 0 and cells.count(X_POINT) >= 3 and cells.count(O_POINT) >= 3:
            draw_result(cells)
            print("Draw")


# start a game
initialize(list(input("Enter cells:")))
