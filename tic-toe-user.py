X_POINT = 'X'
O_POINT = 'O'


def empty_grid():
    return ['_', '_', '_', '_', '_', '_', '_', '_', '_']


def is_draw(grid):
    return grid.count('_') == 0


def draw_grid(cells):
    print("""
---------
| {0} {1} {2} |
| {3} {4} {5} |
| {6} {7} {8} |
---------
""".format(*cells).replace('_', ' '))


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


def is_contains_integers(cells):
    moves = [int(x) for x in cells if x.isdigit()]
    if len(moves) == 2:
        return True
    else:
        return False


def is_valid_sequence(cells):
    moves = [int(x) for x in cells if x.isdigit()]
    if moves[0] <= 3 and moves[1] <= 3:
        return True
    else:
        return False


def can_make_move_here(part_cell, idx):
    return part_cell[idx] == '_'


def make_move(cells, chosen_horizontal, chosen_cell, side):
    first_horizontal = cells[0:3]
    second_horizontal = cells[3:6]
    third_horizontal = cells[6:9]

    if chosen_horizontal == 1:
        if can_make_move_here(first_horizontal, chosen_cell) is True:
            first_horizontal[chosen_cell] = side
        else:
            print("This cell is occupied! Choose another one!")
            return next_move(cells, handle_user_input(input()), side)
    elif chosen_horizontal == 2:
        if can_make_move_here(second_horizontal, chosen_cell) is True:
            second_horizontal[chosen_cell] = side
        else:
            print("This cell is occupied! Choose another one!")
            return next_move(cells, handle_user_input(input()), side)
    else:
        if can_make_move_here(third_horizontal, chosen_cell) is True:
            third_horizontal[chosen_cell] = side
        else:
            print("This cell is occupied! Choose another one!")
            return next_move(cells, handle_user_input(input()), side)

    return first_horizontal + second_horizontal + third_horizontal


def handle_user_input(user_data):
    if is_contains_integers(user_data) is True:
        if is_valid_sequence(user_data) is True:
            return [int(x) for x in user_data if x.isdigit()]
        else:
            print("Coordinates should be from 1 to 3!")
            return handle_user_input(input())
    else:
        print("You should enter numbers!")
        return handle_user_input(input())


def next_move(cells, user_cells, side):
    grid = make_move(cells, user_cells[0], user_cells[1] - 1, side)
    side = swap_turn(side)
    return start_game(grid, side)


def swap_turn(side):
    if side == X_POINT:
        side = O_POINT
    else:
        side = X_POINT

    return side


def start_game(grid, side):
    draw_grid(grid)
    if is_x_wins(grid):
        print("X wins")
    elif is_o_wins(grid):
        print("O wins")
    elif is_draw(grid):
        print("Draw!")
    else:
        next_move(grid, handle_user_input(input()), side)


start_game(empty_grid(), X_POINT)
